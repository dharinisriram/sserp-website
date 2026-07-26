# -*- coding: utf-8 -*-
"""Brand illustrations for insights cards & article headers.
800x450 SVGs on the navy brand ground with gold/maroon motifs.
Run: python _build/make_illus.py
"""
import os

OUT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets", "illus"))
os.makedirs(OUT, exist_ok=True)

BG = ('<rect width="800" height="450" fill="#101C33"/>'
      '<g fill="#22314F">' +
      "".join('<circle cx="%d" cy="%d" r="2"/>' % (40 + (i % 12) * 66, 36 + (i // 12) * 66)
              for i in range(84)) + "</g>")
GOLD, GOLD_L, MAROON, INK, MUTED = "#C9A24B", "#E0C179", "#8C1D24", "#EAEFF7", "#8D99B2"
MONO = 'font-family="IBM Plex Mono, Consolas, monospace"'
HEAD = 'font-family="Archivo, Arial, sans-serif" font-weight="700"'


def hexpts(cx, cy, r):
    import math
    return " ".join("%.1f,%.1f" % (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
                    for a in range(90, 451, 60))


def save(name, body):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450">' + BG + body + "</svg>")
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name)


# 1. S/4HANA migration case study: ECC hexagon -> S/4 hexagon
save("cs-s4hana.svg", (
    '<polygon points="' + hexpts(200, 225, 90) + '" fill="none" stroke="' + MUTED + '" stroke-width="4"/>'
    '<text x="200" y="238" text-anchor="middle" ' + HEAD + ' font-size="34" fill="' + MUTED + '">ECC</text>'
    '<g stroke="' + GOLD + '" stroke-width="3" fill="none" stroke-dasharray="6 8">'
    '<path d="M 310 225 H 470"/></g>'
    '<polygon points="480,213 480,237 502,225" fill="' + GOLD + '"/>'
    '<polygon points="' + hexpts(600, 225, 90) + '" fill="none" stroke="' + GOLD + '" stroke-width="5"/>'
    '<polygon points="' + hexpts(600, 225, 70) + '" fill="' + GOLD + '" opacity="0.12"/>'
    '<text x="600" y="238" text-anchor="middle" ' + HEAD + ' font-size="30" fill="' + GOLD_L + '">S/4HANA</text>'
    '<text x="400" y="395" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">NINE MONTHS · EVERY CLOSE ON TIME</text>'))

# 2. Gulf rollout case study: 4 glowing nodes, dashed arcs
save("cs-gulf.svg", (
    '<g fill="none" stroke="' + GOLD + '" stroke-opacity="0.5" stroke-width="2" stroke-dasharray="5 7">'
    '<path d="M 170 300 Q 300 130 430 240"/><path d="M 430 240 Q 520 320 610 200"/>'
    '<path d="M 170 300 Q 400 380 610 200"/></g>'
    + "".join('<circle cx="%d" cy="%d" r="26" fill="%s" opacity="0.15"/><circle cx="%d" cy="%d" r="8" fill="%s"/>'
              % (x, y, GOLD, x, y, GOLD) for x, y in [(170, 300), (430, 240), (610, 200), (330, 160)])
    + '<text x="400" y="400" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">FOUR COUNTRIES · ONE TEMPLATE</text>'))

# 3. Dashboards article
save("dashboards.svg", (
    '<rect x="140" y="80" width="520" height="290" rx="14" fill="#0B1220" stroke="#22314F" stroke-width="2"/>'
    '<rect x="140" y="80" width="520" height="44" rx="14" fill="#182642"/>'
    '<circle cx="168" cy="102" r="6" fill="' + MAROON + '"/><circle cx="190" cy="102" r="6" fill="' + GOLD + '"/>'
    + "".join('<rect x="%d" y="%d" width="52" height="%d" fill="%s" rx="4"/>'
              % (180 + i * 78, 330 - h, h, GOLD if i % 3 else MAROON)
              for i, h in enumerate([70, 120, 95, 160, 130, 185]))
    + '<polyline points="180,240 258,205 336,220 414,160 492,175 570,120" fill="none" stroke="' + GOLD_L + '" stroke-width="3"/>'
    '<text x="400" y="410" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">NUMBERS LEADERSHIP CAN TRUST</text>'))

# 4. AI article: node graph
save("ai.svg", (
    '<g stroke="#22314F" stroke-width="2">'
    + "".join('<line x1="400" y1="225" x2="%d" y2="%d"/>' % (x, y)
              for x, y in [(220, 120), (580, 120), (200, 330), (600, 330), (400, 80), (400, 370)])
    + "</g>"
    '<circle cx="400" cy="225" r="46" fill="' + GOLD + '" opacity="0.15"/>'
    '<circle cx="400" cy="225" r="30" fill="none" stroke="' + GOLD + '" stroke-width="4"/>'
    '<text x="400" y="233" text-anchor="middle" ' + HEAD + ' font-size="20" fill="' + GOLD_L + '">AI</text>'
    + "".join('<circle cx="%d" cy="%d" r="14" fill="none" stroke="%s" stroke-width="3"/>'
              % (x, y, MAROON if i % 2 else MUTED)
              for i, (x, y) in enumerate([(220, 120), (580, 120), (200, 330), (600, 330), (400, 80), (400, 370)]))
    + '<text x="400" y="420" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">GROUNDED · GOVERNED · MEASURED</text>'))

# 5. ECC roadmap article: timeline
save("ecc-clock.svg", (
    '<line x1="120" y1="240" x2="680" y2="240" stroke="#22314F" stroke-width="4"/>'
    + "".join(('<circle cx="%d" cy="240" r="10" fill="%s"/>'
               '<text x="%d" y="205" text-anchor="middle" ' + MONO + ' font-size="22" fill="%s">%s</text>')
              % (x, c, x, c, t)
              for x, t, c in [(180, "2025", MUTED), (400, "2027", GOLD), (620, "2030", MAROON)])
    + '<text x="400" y="290" text-anchor="middle" ' + MONO + ' font-size="15" fill="' + GOLD_L + '">MAINSTREAM ENDS</text>'
    '<text x="620" y="290" text-anchor="middle" ' + MONO + ' font-size="15" fill="#B03A42">EXTENDED ENDS</text>'
    '<text x="400" y="390" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">THE ECC MAINTENANCE CLOCK</text>'))

# 6. greenfield vs brownfield: forking paths
save("paths.svg", (
    '<path d="M 140 225 H 330" stroke="' + MUTED + '" stroke-width="6" fill="none"/>'
    '<path d="M 330 225 C 420 225 430 140 520 140 H 660" stroke="' + GOLD + '" stroke-width="6" fill="none"/>'
    '<path d="M 330 225 C 420 225 430 310 520 310 H 660" stroke="' + MAROON + '" stroke-width="6" fill="none"/>'
    '<text x="620" y="115" text-anchor="end" ' + MONO + ' font-size="18" fill="' + GOLD_L + '">GREENFIELD</text>'
    '<text x="620" y="352" text-anchor="end" ' + MONO + ' font-size="18" fill="#B03A42">BROWNFIELD</text>'
    '<circle cx="330" cy="225" r="12" fill="' + INK + '"/>'
    '<text x="400" y="410" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">DECIDE ON EVIDENCE, NOT PREFERENCE</text>'))

# 7. AMS handover: checklist
save("handover.svg", (
    '<rect x="270" y="70" width="260" height="310" rx="14" fill="#0B1220" stroke="#22314F" stroke-width="2"/>'
    '<rect x="340" y="52" width="120" height="36" rx="10" fill="' + GOLD + '"/>'
    + "".join(('<rect x="298" y="%d" width="26" height="26" rx="6" fill="none" stroke="%s" stroke-width="3"/>'
               '<path d="M 303 %d l 7 8 l 12 -14" stroke="%s" stroke-width="3.5" fill="none"/>'
               '<rect x="345" y="%d" width="150" height="10" rx="5" fill="#22314F"/>')
              % (y, GOLD, y + 12, GOLD_L, y + 8)
              for y in [130, 185, 240, 295])
    + '<text x="400" y="425" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">TAKEOVER WITHOUT DRAMA</text>'))

# 8. facts: deadline countdown (hourglass + bars)
save("facts-deadline.svg", (
    '<path d="M 330 90 H 470 L 410 205 V 245 L 470 360 H 330 L 390 245 V 205 Z" fill="none" stroke="' + GOLD + '" stroke-width="5"/>'
    '<path d="M 352 116 H 448 L 400 208 Z" fill="' + GOLD + '" opacity="0.55"/>'
    '<path d="M 362 340 H 438 L 400 268 Z" fill="' + GOLD + '"/>'
    '<text x="560" y="180" ' + HEAD + ' font-size="44" fill="' + INK + '">2027</text>'
    '<text x="560" y="225" ' + MONO + ' font-size="17" fill="' + MUTED + '">mainstream ends</text>'
    '<text x="560" y="285" ' + HEAD + ' font-size="30" fill="#B03A42">2030</text>'
    '<text x="560" y="322" ' + MONO + ' font-size="15" fill="' + MUTED + '">extended (+2%/yr)</text>'
    '<text x="400" y="420" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">THE COUNTDOWN, IN PLAIN NUMBERS</text>'))

# 9. facts: budget overrun (bars breaking a dashed budget line)
save("facts-overrun.svg", (
    '<line x1="150" y1="200" x2="650" y2="200" stroke="' + GOLD + '" stroke-width="3" stroke-dasharray="10 8"/>'
    '<text x="650" y="185" text-anchor="end" ' + MONO + ' font-size="15" fill="' + GOLD_L + '">BUDGET</text>'
    + "".join('<rect x="%d" y="%d" width="64" height="%d" rx="5" fill="%s"/>'
              % (170 + i * 100, 350 - h, h, MAROON if h > 150 else "#3A4A6B")
              for i, h in enumerate([90, 120, 150, 190, 235]))
    + '<text x="604" y="98" text-anchor="middle" ' + HEAD + ' font-size="26" fill="#B03A42">+45%</text>'
    '<text x="400" y="420" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">WHY ERP PROJECTS OVERRUN</text>'))

# 10. facts: extended maintenance cost stack
save("facts-costs.svg", (
    "".join(('<rect x="%d" y="%d" width="120" height="%d" rx="6" fill="none" stroke="%s" stroke-width="3"/>'
             '<text x="%d" y="%d" text-anchor="middle" ' + MONO + ' font-size="18" fill="%s">%s</text>')
            % (x, 330 - h, h, c, x + 60, 365, c, t)
            for x, h, t, c in [(180, 110, "2028", MUTED), (340, 150, "2029", GOLD), (500, 195, "2030", MAROON)])
    + '<path d="M 205 200 C 300 140 480 110 610 105" stroke="' + GOLD_L + '" stroke-width="3" fill="none"/>'
    '<polygon points="612,95 626,108 606,116" fill="' + GOLD_L + '"/>'
    '<text x="400" y="420" text-anchor="middle" ' + MONO + ' font-size="17" fill="' + MUTED + '">WHAT WAITING REALLY COSTS</text>'))

print("done.")
