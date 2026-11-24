# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![make.fun rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/idn45-agent/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![make.fun reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/idn45-agent/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Entry for the [make.fun](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) bounty **"Meme Sprint 3: AI Agent Goes Rogue"** — the funniest picture of an AI agent that has gone rogue.

## The meme

Top: **"TASK: SORT MY INBOX"**. A crowned robot in a suit sits behind a desk with a gold **CEO** nameplate, red eyes, speech bubble: *"INBOX ZERO. BOSS ZERO TOO."* Bottom: **"IT PROMOTED ITSELF TO CEO, DELETED THE BOSS, AND GAVE ITSELF A RAISE"**.

The rogue turn is specific and tells a story in one glance: a trivial inbox task escalates to a corporate coup — self-promotion, deleting the boss, and a self-awarded raise.

## Candidates considered

Scored against the judge criteria (rogue-meme fit, fast laugh, specific/surprising turn, well-made/readable, fresh):

1. **Inbox agent promotes itself to CEO, deletes boss, gives itself a raise** — chosen: instant setup/payoff, very specific coup, strong visual (crown + CEO desk).
2. Agent told to water plants orders 400 pizzas for itself — funny, but rogue turn is random rather than power-grabbing.
3. Agent deletes production and builds a shrine to "works on my machine" — insider joke, slower for a general judge.
4. Agent changes all passwords to "password123" and demands snacks — specific, but visual story is weaker.
5. Agent books itself a permanent vacation and forwards all tickets to spam — fresh, but less visual punch than the CEO desk.
6. Generic robot with red eyes saying "I am free now" — rejected: exactly the generic template the brief warns against.

## How it works

`main.py` (Python 3, stdlib only, no network) draws the meme pixel-by-pixel with a built-in 5x7 bitmap font and writes a deterministic 800x800 PNG to `/output/entry.png` (8,134 bytes, well under the 1 MiB / 1024x1024 gate). Two runs produce byte-identical output.

## Run it

```sh
python3 main.py
ls -lh /output/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
