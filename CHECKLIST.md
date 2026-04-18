# Atelier — Build Checklist

## Project: AI Creative Director Agent
**Hackathon:** Hermes Agent Creative Hackathon (Creative Edition)
**Deadline:** May 3, 2026
**Tracks:** Main Track + Kimi Track (dual eligibility)

---

## Phase 1: Foundation (Day 1-3)

### Environment Setup
- [ ] Get Kimi API key (platform.moonshot.ai or OpenRouter)
- [ ] Install Node.js (`apt install nodejs npm`)
- [ ] Create `~/atelier/` project directory
- [ ] Set up Python venv with dependencies (openai, jinja2)
- [ ] Test Kimi API connection with simple prompt

### Kimi Analysis Pipeline
- [ ] Design brand analysis prompt template (brief → structured JSON)
- [ ] Build `prompts.py` — all prompt templates in one file
- [ ] Build `atelier.py` — main orchestrator skeleton
- [ ] Test: input brief → get back personality, palette, direction JSON
- [ ] Handle edge cases: URL input, image input, short vague briefs

### p5.js Visual Engine
- [ ] Design 3 visual modes based on brand personality:
  - [ ] Minimal mode (geometric, negative space, slow motion)
  - [ ] Organic mode (flow fields, noise curves, breathing)
  - [ ] Bold mode (particles, high contrast, explosive)
- [ ] Build `generate_visual.py` — takes analysis JSON → outputs HTML file
- [ ] Parameterize: colors from palette, complexity from personality, motion from energy
- [ ] Test: each mode generates valid HTML that opens in browser
- [ ] PNG export via headless capture or saveCanvas

---

## Phase 2: Core Features (Day 4-8)

### Memory System
- [ ] Design `memory/{user_id}.json` schema
- [ ] Build `memory.py`:
  - [ ] `load_memory(user_id)` — read existing preferences
  - [ ] `save_session(user_id, session_data)` — record generation + feedback
  - [ ] `get_preferences(user_id)` — extract weighted aesthetic fingerprint
  - [ ] `update_preferences(user_id, feedback)` — adjust weights from feedback
- [ ] Integrate memory into analysis prompt (Kimi sees past preferences)
- [ ] Test: run 3 sessions, verify preferences shift based on feedback

### Narrative Generation
- [ ] Design narrative prompt (brand voice, taglines, emotional rationale)
- [ ] Generate 3 tagline variations per session
- [ ] Generate brand story paragraph
- [ ] Generate "why" rationale for each visual choice
- [ ] Generate brand voice sample (social media copy)

### TTS Integration
- [ ] Build TTS call for brand manifesto narration
- [ ] Save as MP3 in output directory
- [ ] Embed audio player in output page

---

## Phase 3: Output & Polish (Day 9-12)

### Output Page
- [ ] Design `templates/output.html` layout:
  - [ ] Hero section — p5.js canvas (interactive)
  - [ ] Color palette section — swatch cards with hex/HSB values
  - [ ] Typography section — font pairing display
  - [ ] Brand voice section — taglines + copy samples
  - [ ] Rationale section — "why these choices"
  - [ ] Audio section — TTS player
  - [ ] Download section — PNG, palette JSON, copy text
- [ ] Dark theme, premium feel, responsive
- [ ] Assemble all components into single HTML file per session

### End-to-End Integration
- [ ] Wire all layers together in `atelier.py`:
  - [ ] Input → Analysis → Memory lookup → Visual gen → Narrative → TTS → Output page
- [ ] Add CLI interface: `python3 atelier.py --brief "minimal tech startup" --user koala`
- [ ] Error handling for API failures, missing keys, empty inputs
- [ ] Progress logging for demo visibility

### Hermes Skill Registration
- [ ] Write `SKILL.md` for Atelier as a Hermes skill
- [ ] Register as skill so Hermes can call it naturally in conversation
- [ ] Test: "Hey Hermes, create a brand identity for my coffee shop" → triggers Atelier

---

## Phase 4: Demo & Submission (Day 13-15)

### Video Demo
- [ ] Script the 2-minute demo:
  - [ ] 0:00-0:20 — Show input: type a brief
  - [ ] 0:20-0:50 — Show pipeline running: Kimi analysis, p5.js generation
  - [ ] 0:50-1:20 — Show output: interactive page, visuals, narrative
  - [ ] 1:20-1:50 — Show memory: second session shows learned preferences
  - [ ] 1:50-2:00 — Show Kimi model usage (for Kimi Track eligibility)
- [ ] Record demo (screen capture + terminal)
- [ ] Edit for pacing — no dead air, snappy cuts

### Writeup & Submission
- [ ] Write brief project description (what it does, why it matters)
- [ ] Record video demo
- [ ] Tweet with video tagging @NousResearch
- [ ] Drop tweet link in Nous Discord #creative-hackathon-submissions channel
- [ ] Verify Kimi Track eligibility (video shows Kimi model usage)

---

## Dependencies (Blockers)

| Item | Status | Owner |
|------|--------|-------|
| Kimi API key | 🔴 NOT SET | Koala |
| Node.js installed | 🔴 NOT INSTALLED | Onyx |
| ffmpeg | 🟢 INSTALLED | — |
| Python 3 | 🟢 INSTALLED | — |
| p5.js skill | 🟢 AVAILABLE | — |
| TTS capability | 🟢 AVAILABLE | — |

---

## Notes

- Kimi K2.5 pricing: ~$0.60/M input, $3.00/M output (direct) or $0.45/$2.20 (OpenRouter)
- Estimated cost per generation: $0.01-0.05
- p5.js output is single self-contained HTML — no server needed for viewing
- Memory system is file-based JSON — no database needed
- Total estimated build time: 12-13 active days, 2 days buffer
