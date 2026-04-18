# Atelier

AI Creative Director Agent — Hermes Agent Creative Hackathon (Creative Edition)

Give Atelier a brief. It generates a complete creative identity: generative visuals, color palette, brand narrative, and spoken manifesto. Then it remembers what you liked and gets better at understanding your taste over time.

**Live:** [atelier.ko4lax.dev](https://atelier.ko4lax.dev)

## What it does

1. **Analyze** — Kimi K2.5 reads your brief and extracts brand personality, visual direction, and target aesthetic
2. **Generate** — p5.js creates unique generative art patterns based on the analysis
3. **Narrate** — Kimi writes taglines, brand story, and explains *why* each visual choice was made
4. **Speak** — TTS produces a spoken brand manifesto
5. **Remember** — Your preferences are saved. Next session produces output more aligned with your taste

## Tracks

- **Main Track** ($10k / $3.5k / $1.5k)
- **Kimi Track** ($3.5k / $1k / $500) — uses Kimi K2.5 for analysis and narrative

## Quick start

```bash
# Set your Kimi API key
export MOONSHOT_API_KEY="your-key-here"

# Generate a brand identity
python3 src/atelier.py --brief "minimal tech startup for remote workers" --user koala
```

## Architecture

```
User Brief (text/URL)
        │
        ▼
┌─────────────────────┐
│  Kimi Analysis       │  brief → personality, palette, direction
├─────────────────────┤
│  Memory Lookup       │  past preferences → generation weights
├─────────────────────┤
│  Visual Generation   │  p5.js patterns, color system, textures
├─────────────────────┤
│  Narrative Generation│  taglines, brand story, emotional rationale
├─────────────────────┤
│  TTS Narration       │  spoken brand manifesto
├─────────────────────┤
│  Output Assembly     │  interactive HTML page
├─────────────────────┤
│  Memory Save         │  record session + learn
└─────────────────────┘
```

## Built for

The [Hermes Agent Creative Hackathon](https://x.com/NousResearch/status/2045225469088326039) — Creative Edition
Presented by Kimi Moonshot & Nous Research

## License

MIT
