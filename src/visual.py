"""
Visual generation for Atelier — p5.js generative art based on brand analysis.
"""

import os
import json


# Visual mode templates (inline p5.js HTML)
VISUAL_MODES = {
    "minimal": {
        "description": "Geometric compositions with clean lines, negative space, and controlled motion",
        "template": "minimal",
    },
    "organic": {
        "description": "Flowing curves, noise-driven patterns, breathing animations, natural textures",
        "template": "organic",
    },
    "bold": {
        "description": "High contrast, particle systems, dynamic motion, explosive energy",
        "template": "bold",
    },
}


def hue_to_hex(hue, sat=70, bri=85):
    """Convert HSB to approximate hex color."""
    import colorsys
    h = hue / 360.0
    s = sat / 100.0
    v = bri / 100.0
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"


def generate_palette_colors(analysis):
    """Generate a full color palette from analysis."""
    palette = analysis.get("palette", {})
    primary_hue = palette.get("primary_hue", 210)
    secondary_hue = palette.get("secondary_hue", (primary_hue + 30) % 360)
    accent_hue = palette.get("accent_hue", (primary_hue + 180) % 360)
    sat = palette.get("saturation", 50)
    bri = palette.get("brightness", 80)

    return {
        "bg": hue_to_hex(primary_hue, max(10, sat - 40), max(8, bri - 70)),
        "primary": hue_to_hex(primary_hue, sat, bri),
        "secondary": hue_to_hex(secondary_hue, max(20, sat - 15), bri),
        "accent": hue_to_hex(accent_hue, min(100, sat + 20), bri),
        "text": hue_to_hex(primary_hue, 15, 95),
        "muted": hue_to_hex(primary_hue, max(5, sat - 30), max(30, bri - 30)),
    }


def _minimal_template(colors, analysis):
    """Minimal p5.js visual — geometric, clean, spacious."""
    complexity = analysis.get("complexity", 0.5)
    energy = analysis.get("energy", 0.3)
    motion = analysis.get("motion_style", "slow-drift")

    num_shapes = int(5 + complexity * 15)
    speed = 0.2 + energy * 0.8
    has_motion = motion != "static"

    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<title>Atelier — Minimal</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.11.3/p5.min.js"></script>
<style>html,body{{margin:0;padding:0;overflow:hidden;background:{colors["bg"]};}}</style>
</head><body><script>
p5.disableFriendlyErrors = true;
const C = {json.dumps(colors)};
const N = {num_shapes};
const SPEED = {speed};
const MOTION = {str(has_motion).lower()};
let shapes = [];

function setup() {{
  createCanvas(windowWidth, windowHeight);
  colorMode(HSB, 360, 100, 100, 100);
  noStroke();
  for (let i = 0; i < N; i++) {{
    shapes.push({{
      x: random(width * 0.15, width * 0.85),
      y: random(height * 0.15, height * 0.85),
      size: random(40, min(width, height) * 0.25),
      type: floor(random(3)),
      phase: random(TWO_PI),
      speed: random(0.3, 1) * SPEED,
      hueShift: random(-20, 20),
    }});
  }}
}}

function draw() {{
  background("{colors["bg"]}");
  let t = MOTION ? millis() * 0.001 : 0;

  for (let s of shapes) {{
    push();
    let ox = MOTION ? sin(t * s.speed + s.phase) * 20 : 0;
    let oy = MOTION ? cos(t * s.speed * 0.7 + s.phase) * 15 : 0;
    translate(s.x + ox, s.y + oy);

    // Shadow
    fill(0, 0, 0, 8);
    if (s.type === 0) ellipse(4, 4, s.size);
    else if (s.type === 1) rect(-s.size/2 + 4, -s.size/2 + 4, s.size, s.size);
    else rect(-s.size/2 + 4, -s.size/3 + 4, s.size, s.size * 0.66);

    // Shape
    fill("{colors["primary"]}");
    if (s.type === 0) ellipse(0, 0, s.size);
    else if (s.type === 1) rect(-s.size/2, -s.size/2, s.size, s.size);
    else rect(-s.size/2, -s.size/3, s.size, s.size * 0.66);
    pop();
  }}

  // Accent line
  stroke("{colors["accent"]}");
  strokeWeight(1);
  let lx = width * 0.3 + (MOTION ? sin(t * 0.5) * 50 : 0);
  line(lx, height * 0.2, lx, height * 0.8);
  noStroke();
}}

function windowResized() {{ resizeCanvas(windowWidth, windowHeight); }}
function keyPressed() {{ if (key === 's') saveCanvas('atelier-minimal', 'png'); }}
</script></body></html>'''


def _organic_template(colors, analysis):
    """Organic p5.js visual — flow fields, curves, breathing."""
    complexity = analysis.get("complexity", 0.5)
    energy = analysis.get("energy", 0.5)

    num_particles = int(200 + complexity * 500)
    noise_scale = 0.003 + (1 - complexity) * 0.005

    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<title>Atelier — Organic</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.11.3/p5.min.js"></script>
<style>html,body{{margin:0;padding:0;overflow:hidden;background:{colors["bg"]};}}</style>
</head><body><script>
p5.disableFriendlyErrors = true;
const C = {json.dumps(colors)};
const N = {num_particles};
const NS = {noise_scale};
let particles = [];

function setup() {{
  createCanvas(windowWidth, windowHeight);
  colorMode(HSB, 360, 100, 100, 100);
  for (let i = 0; i < N; i++) {{
    particles.push({{
      x: random(width), y: random(height),
      hue: random(-15, 15), alpha: random(15, 40),
      life: random(100, 400), age: 0,
    }});
  }}
  background("{colors["bg"]}");
}}

function draw() {{
  // Fade background
  background("{colors["bg"]}");
  let t = millis() * 0.0003;

  for (let p of particles) {{
    let angle = noise(p.x * NS, p.y * NS, t) * TWO_PI * 2;
    p.x += cos(angle) * 1.5;
    p.y += sin(angle) * 1.5;
    p.age++;

    // Wrap
    if (p.x < 0) p.x = width;
    if (p.x > width) p.x = 0;
    if (p.y < 0) p.y = height;
    if (p.y > height) p.y = 0;

    // Reset dead particles
    if (p.age > p.life) {{
      p.x = random(width); p.y = random(height);
      p.age = 0; p.life = random(100, 400);
    }}

    let a = p.alpha * (1 - p.age / p.life);
    stroke((210 + p.hue) % 360, 45, 85, a);
    strokeWeight(1.2);
    point(p.x, p.y);
  }}
}}

function windowResized() {{ resizeCanvas(windowWidth, windowHeight); background("{colors["bg"]}"); }}
function keyPressed() {{ if (key === 's') saveCanvas('atelier-organic', 'png'); }}
</script></body></html>'''


def _bold_template(colors, analysis):
    """Bold p5.js visual — particles, high contrast, explosive."""
    complexity = analysis.get("complexity", 0.5)
    energy = analysis.get("energy", 0.8)

    num_particles = int(100 + complexity * 300)

    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<title>Atelier — Bold</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.11.3/p5.min.js"></script>
<style>html,body{{margin:0;padding:0;overflow:hidden;background:{colors["bg"]};}}</style>
</head><body><script>
p5.disableFriendlyErrors = true;
const C = {json.dumps(colors)};
const N = {num_particles};
let particles = [];

function setup() {{
  createCanvas(windowWidth, windowHeight);
  colorMode(HSB, 360, 100, 100, 100);
  for (let i = 0; i < N; i++) {{
    particles.push({{
      x: width/2, y: height/2,
      vx: random(-6, 6), vy: random(-6, 6),
      size: random(3, 12),
      hue: random([0, 30, 180, 210, 330]),
      life: random(60, 200), age: 0,
    }});
  }}
  background("{colors["bg"]}");
}}

function draw() {{
  background("{colors["bg"]}");

  for (let i = particles.length - 1; i >= 0; i--) {{
    let p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    p.vx *= 0.99;
    p.vy *= 0.99;
    p.age++;

    let a = 80 * (1 - p.age / p.life);
    fill(p.hue, 80, 95, a);
    noStroke();
    ellipse(p.x, p.y, p.size * (1 - p.age/p.life * 0.5));

    if (p.age > p.life || p.x < -50 || p.x > width+50 || p.y < -50 || p.y > height+50) {{
      particles.splice(i, 1);
      particles.push({{
        x: width/2 + random(-30,30), y: height/2 + random(-30,30),
        vx: random(-6, 6), vy: random(-6, 6),
        size: random(3, 12),
        hue: random([0, 30, 180, 210, 330]),
        life: random(60, 200), age: 0,
      }});
    }}
  }}

  // Center glow
  noStroke();
  for (let r = 60; r > 0; r -= 3) {{
    fill("{colors["accent"]}".replace("#",""));
    fill(0, 60, 95, 2);
    ellipse(width/2, height/2, r*2);
  }}
}}

function windowResized() {{ resizeCanvas(windowWidth, windowHeight); }}
function keyPressed() {{
  if (key === 's') saveCanvas('atelier-bold', 'png');
  if (key === ' ') {{
    for (let p of particles) {{
      p.vx = random(-8, 8); p.vy = random(-8, 8);
    }}
  }}
}}
</script></body></html>'''


TEMPLATES = {
    "minimal": _minimal_template,
    "organic": _organic_template,
    "bold": _bold_template,
}


def generate_visual(analysis, output_dir):
    """Generate p5.js visual from brand analysis. Returns info dict."""
    personality = analysis.get("brand_personality", "minimal")

    # Map personality to visual mode
    mode_map = {
        "minimal": "minimal",
        "technical": "minimal",
        "luxurious": "minimal",
        "organic": "organic",
        "warm": "organic",
        "bold": "bold",
        "edgy": "bold",
        "playful": "bold",
    }
    mode = mode_map.get(personality, "minimal")
    colors = generate_palette_colors(analysis)
    template_fn = TEMPLATES[mode]
    html = template_fn(colors, analysis)

    # Write HTML
    filepath = os.path.join(output_dir, "visual.html")
    with open(filepath, "w") as f:
        f.write(html)

    # Write palette
    palette_path = os.path.join(output_dir, "palette.json")
    with open(palette_path, "w") as f:
        json.dump(colors, f, indent=2)

    return {
        "file": filepath,
        "mode": mode,
        "colors": colors,
        "description": VISUAL_MODES[mode]["description"],
    }
