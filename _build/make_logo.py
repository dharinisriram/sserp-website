# -*- coding: utf-8 -*-
"""Reconstruct the SS ERP interlocking-S hexagon mark as precise vector art.
The mark is 180-degree rotationally symmetric: one ribbon path drawn twice
(maroon as-is, gold rotated 180 about the centre), plus the pixel sparkle.
Geometry: pointy-top hexagon; each ribbon = edge hook + centre bar; the two
bars are parallel strips offset g/2 either side of the main diagonal, giving
the even interlock slits of the original lockup.
Outputs assets/logo.svg (mark) and assets/logo-lockup.svg (mark + wordmark).
"""
import math
import os

ASSETS = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets"))

CX, CY, R = 100.0, 100.0, 92.0
W = 24.0     # ribbon thickness
G = 7.0      # interlock slit width
CUT = 0.62   # fraction of top-right edge covered before the ribbon's cut
X_END = 148.0  # x where the centre bar ends (tucks into the opposite hook)

COS30, SIN30 = math.cos(math.radians(30)), 0.5

def vtx(deg):
    rad = math.radians(deg)
    return (CX + R * math.cos(rad), CY - R * math.sin(rad))

T, TL, BL, B, BR, TR = vtx(90), vtx(150), vtx(210), vtx(270), vtx(330), vtx(30)

def lerp(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)

def on_line(anchor, x):
    """Point on a line through `anchor` with direction (cos30, -sin30), at given x."""
    t = (x - anchor[0]) / COS30
    return (x, anchor[1] - t * SIN30)

# bar edge lines: main diagonal offset up-left by g/2 (lower edge) and g/2+W (upper edge)
N_UP = (-SIN30, -COS30)                     # up-left normal of the bar direction
A_LOW = (CX + N_UP[0] * (G / 2), CY + N_UP[1] * (G / 2))
A_UP = (CX + N_UP[0] * (G / 2 + W), CY + N_UP[1] * (G / 2 + W))

# outer cut on the top-right edge + its inner corner
S1 = lerp(T, TR, CUT)
S1i = (S1[0] - W * SIN30, S1[1] + W * COS30)

# inner hexagon reference points
X_IN = TL[0] + W                            # inner left edge
A_in = (CX, T[1] + W / COS30)               # inner apex
tq = (A_in[0] - X_IN) / COS30
Q = (X_IN, A_in[1] + tq * SIN30)            # inner TL edge meets inner left edge

def intersect(p1, d1, p2, d2):
    """Intersection of lines p1+t*d1 and p2+u*d2."""
    den = d1[0] * d2[1] - d1[1] * d2[0]
    t = ((p2[0] - p1[0]) * d2[1] - (p2[1] - p1[1]) * d2[0]) / den
    return (p1[0] + t * d1[0], p1[1] + t * d1[1])

# tail: left edge ends at a cut parallel to the bottom-left hexagon edge,
# offset G above it; the cut runs to the bar's lower edge (chevron tip)
E_BL = (COS30, SIN30)                       # bottom-left edge direction BL->B
N_EDGE_UP = (SIN30, -COS30)                 # upward normal of that edge
P0 = (BL[0] + N_EDGE_UP[0] * G, BL[1] + N_EDGE_UP[1] * G)
D_BAR = (COS30, -SIN30)
TAIL_TOP = intersect(P0, E_BL, (TL[0], 0.0), (0.0, 1.0))
TIP = intersect(P0, E_BL, A_LOW, D_BAR)

# bar end (vertical cut, parallel to the hexagon's right edge)
E_out = on_line(A_LOW, X_END)
E_in = on_line(A_UP, X_END)
# bar upper edge back to the inner left edge
C1 = on_line(A_UP, X_IN)

pts = [S1, T, TL, TAIL_TOP, TIP, E_out, E_in, C1, Q, A_in, S1i]
path = "M " + " L ".join("%.2f %.2f" % p for p in pts) + " Z"

sparkle = """
  <rect x="152" y="26" width="11" height="11" fill="url(#gmaroon)"/>
  <rect x="167" y="12" width="9" height="9" fill="url(#ggold)"/>
  <rect x="170" y="34" width="7" height="7" fill="url(#ggold)"/>
  <rect x="158" y="3" width="6" height="6" fill="url(#ggold)"/>
"""

DEFS = """<defs>
    <linearGradient id="gmaroon" x1="0%" y1="0%" x2="85%" y2="100%">
      <stop offset="0%" stop-color="#B01E28"/>
      <stop offset="55%" stop-color="#8C1D24"/>
      <stop offset="100%" stop-color="#5E1015"/>
    </linearGradient>
    <linearGradient id="ggold" x1="15%" y1="0%" x2="90%" y2="100%">
      <stop offset="0%" stop-color="#EBCB84"/>
      <stop offset="50%" stop-color="#C9A24B"/>
      <stop offset="100%" stop-color="#A67C24"/>
    </linearGradient>
  </defs>"""

MARK_BODY = DEFS + """
  <path d="{path}" fill="url(#gmaroon)"/>
  <path d="{path}" fill="url(#ggold)" transform="rotate(180 {cx} {cy})"/>
""".format(path=path, cx=CX, cy=CY) + sparkle

logo = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">\n  '
        + MARK_BODY + "\n</svg>\n")
with open(os.path.join(ASSETS, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo)
print("wrote assets/logo.svg")

lockup = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 220" '
          'font-family="Archivo, Arial, sans-serif">\n  '
          '<g transform="translate(10 10)">' + MARK_BODY + "</g>\n"
          '  <line x1="248" y1="30" x2="248" y2="190" stroke="#C9A24B" stroke-width="3"/>\n'
          '  <text x="278" y="98" font-size="56" font-weight="800">'
          '<tspan fill="#8C1D24">SS </tspan><tspan fill="#1B2437">ERP Solutions</tspan></text>\n'
          '  <text x="280" y="140" font-size="30" font-weight="500" fill="#C9A24B">'
          'Enterprise Technology Consulting</text>\n'
          '  <text x="280" y="178" font-size="17" font-weight="600" letter-spacing="3" fill="#1B2437">'
          'IMPLEMENT <tspan fill="#8C1D24">|</tspan> OPTIMIZE <tspan fill="#8C1D24">|</tspan> TRANSFORM</text>\n'
          "</svg>\n")
with open(os.path.join(ASSETS, "logo-lockup.svg"), "w", encoding="utf-8") as f:
    f.write(lockup)
print("wrote assets/logo-lockup.svg")
