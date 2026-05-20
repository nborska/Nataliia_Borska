#!/bin/bash
set -euo pipefail

# Only run in remote Claude Code environment
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

SKILLS_DIR="$HOME/.claude/skills"
mkdir -p "$SKILLS_DIR"

install_skill() {
  local name=$1
  local url=$2
  if [ ! -d "$SKILLS_DIR/$name" ]; then
    echo "Installing skill: $name"
    git clone --depth=1 "$url" "$SKILLS_DIR/$name" 2>/dev/null
  fi
}

install_skill "claude-seo"          "https://github.com/AgriciDaniel/claude-seo"
install_skill "social-media-skills"  "https://github.com/charlie947/social-media-skills"
install_skill "ai-marketing-skills"  "https://github.com/BrianRWagner/ai-marketing-claude-code-skills"
install_skill "marketingskills"      "https://github.com/coreyhaines31/marketingskills"
install_skill "claude-skills"        "https://github.com/alirezarezvani/claude-skills"
install_skill "creatomate"           "https://github.com/Sara-Saraireh/claude-code-skill-creatomate"
install_skill "seo-geo-skills"       "https://github.com/aaron-he-zhu/seo-geo-claude-skills"
install_skill "openclaudia"          "https://github.com/OpenClaudia/openclaudia-skills"
install_skill "video-toolkit"        "https://github.com/digitalsamba/claude-code-video-toolkit"

echo "All skills ready."
