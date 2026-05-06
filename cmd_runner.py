import json, subprocess, time, os

REPO = os.path.dirname(os.path.abspath(__file__))
PENDING = os.path.join(REPO, "cmds", "pending.json")
RESULT = os.path.join(REPO, "cmds", "result.json")

last_id = ""

while True:
    try:
        # Pull latest changes from GitHub
        os.system(f'cd "{REPO}" && git pull --quiet 2>/dev/null')

        with open(PENDING) as f:
            data = json.load(f)
        cmd_id = data.get("id", "")
        command = data.get("command", "")

        if cmd_id and cmd_id != last_id and command:
            last_id = cmd_id
            try:
                out = subprocess.check_output(
                    command, shell=True, stderr=subprocess.STDOUT, timeout=30,
                    cwd=REPO
                )
                result = out.decode("utf-8", errors="replace")
            except subprocess.CalledProcessError as e:
                result = f"ERROR:\n{e.output.decode('utf-8', errors='replace')}"
            except subprocess.TimeoutExpired:
                result = "ERROR: Command timed out"

            with open(RESULT, "w") as f:
                json.dump({"id": cmd_id, "result": result}, f, ensure_ascii=False, indent=2)

            os.system(
                f'cd "{REPO}" && git add cmds/result.json && '
                f'git commit -m "result {cmd_id}" && git push --quiet 2>/dev/null'
            )
    except Exception:
        pass

    time.sleep(5)
