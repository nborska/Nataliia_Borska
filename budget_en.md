# BUDGET — API cost by number of users

> Estimate of Claude API (Anthropic) cost. DigitalOcean server — fixed $6/mo.
> Main cost driver: the bot's "brain" (~60,000 tokens) sent with every message.

## ASSUMPTIONS
```
Model: Claude Sonnet (quality/price balance)
  input $3 / M tokens · output $15 / M
  cache write $3.75/M · cache read $0.30/M (knowledge cache already enabled)
Knowledge base (brain): ~60,000 tokens (sent with every message)
Cache lives 5 min → within an active session knowledge is cheap (read),
  but the first message of a session pays a cache-write (~$0.22).
```

## COST PER MESSAGE
```
In a session (several in a row): ~$0.05–0.07
Single message (>5 min gap):     ~$0.20–0.25 (pricier — cache rewritten)
Realistic average:               ~$0.07 per message
```

## COST PER USER / MONTH
```
Light usage   (~40 messages/mo):  ~$3
Medium        (~150 messages/mo): ~$11
Heavy (daily) (~400 messages/mo): ~$28
```

## TOTAL BUDGET / MONTH (current code)
```
Users │ Light   │ Medium  │ Heavy
──────────────────────────────────
  10  │  $30    │  $110   │  $280
  50  │  $150   │  $550   │  $1,400
 100  │  $300   │  $1,100 │  $2,800
 500  │  $1,500 │  $5,500 │  $14,000
1000  │  $3,000 │  $11,000│  $28,000
+ server $6/mo (fixed)
```

## OPTIMIZATION (can cut cost 2–4×!)
```
1. Don't send the WHOLE brain every time — load only the relevant
   mode/section (RAG or per-mode). Brain 60k → ~15-20k tokens. ~3× savings.
2. Haiku for simple replies (4× cheaper), Sonnet only for content
   generation. Big savings.
3. 1-hour cache for active users (fewer rewrites).
4. Trim the knowledge base itself (remove duplicates).

AFTER OPTIMIZATION (÷~3):
  Medium per user: ~$4/mo instead of $11
  100 users medium: ~$370/mo instead of $1,100
```

## PRICING TAKEAWAY
```
• A $20-30/mo subscription per client covers a medium user with margin
  (API ~$11 now, ~$4 after optimization).
• Heavy users — separate tier or message cap.
• Optimize the brain first (÷3) — the biggest profitability lever.
```
