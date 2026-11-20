"""Draw the GTA 6 pre-order receipt meme, 1080x1080, with PIL only.
Joke: a GTA VI pre-order receipt paid in full in 2013, finally delivered
13 years later. The make.fun ghost is drawn in-scene as the cashier,
holding its magenta star coin, next to the receipt."""
from PIL import Image, ImageDraw, ImageFont
import math

W = H = 1080
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
MONO_R = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def text_center(d, y, s, f, fill, x0=0, x1=W):
    w = d.textlength(s, font=f)
    d.text(((x0 + x1 - w) / 2, y), s, font=f, fill=fill)

def sparkle(d, cx, cy, r, fill):
    # 4-point star: diamond with concave sides approximated by polygon
    pts = [(cx, cy - r), (cx + r * 0.22, cy - r * 0.22), (cx + r, cy),
           (cx + r * 0.22, cy + r * 0.22), (cx, cy + r),
           (cx - r * 0.22, cy + r * 0.22), (cx - r, cy),
           (cx - r * 0.22, cy - r * 0.22)]
    d.polygon(pts, fill=fill)

def draw_ghost(d, x, y, w, h):
    """White ghost, thick black outline, sparkle eyes, round hand holding
    a magenta coin with a white star. Origin top-left of bounding box."""
    # body: rounded-top shape with wavy hem, drawn as polygon + arcs
    top = y + h * 0.22
    body = [(x, y + h * 0.92), (x, top + h * 0.18)]
    # black silhouette behind (slightly larger), then white body on top
    hem_y = y + h * 0.88
    d.ellipse([x - 6, y - 6, x + w + 6, y + h * 0.55 + 6], fill="black")
    d.rectangle([x - 6, y + h * 0.25, x + w + 6, hem_y + 6], fill="black")
    for i in range(4):
        cx = x + i * w / 4 + w / 8
        r = w / 8
        d.ellipse([cx - r - 6, hem_y - r - 6, cx + r + 6, hem_y + r + 6],
                  fill="black")
    # white body, flat bottom
    d.ellipse([x, y, x + w, y + h * 0.55], fill="white")
    d.rectangle([x, y + h * 0.25, x + w, hem_y], fill="white")
    # wavy hem: white circles overlapping the body's bottom edge, with
    # only their lower arcs outlined in black (no gap, no band)
    for i in range(4):
        cx = x + i * w / 4 + w / 8
        d.ellipse([cx - w / 8, hem_y - w / 8, cx + w / 8, hem_y + w / 8],
                  fill="white")
    for i in range(4):
        cx = x + i * w / 4 + w / 8
        d.arc([cx - w / 8, hem_y - w / 8, cx + w / 8, hem_y + w / 8],
              0, 180, fill="black", width=6)
    # eyes: black 4-point sparkles
    sparkle(d, x + w * 0.36, y + h * 0.30, 26, "black")
    sparkle(d, x + w * 0.64, y + h * 0.30, 26, "black")
    # round hand + magenta coin with white star, at right side
    coin_cx, coin_cy, coin_r = x + w * 0.92, y + h * 0.62, 52
    d.ellipse([coin_cx - coin_r - 8, coin_cy - coin_r - 8,
               coin_cx + coin_r + 8, coin_cy + coin_r + 8], fill="black")
    d.ellipse([coin_cx - coin_r, coin_cy - coin_r,
               coin_cx + coin_r, coin_cy + coin_r], fill="#E5007E")
    sparkle(d, coin_cx, coin_cy, 30, "white")
    # small white hand circle overlapping coin edge
    d.ellipse([x + w * 0.78 - 22, y + h * 0.60 - 22,
               x + w * 0.78 + 22, y + h * 0.60 + 22], fill="white",
              outline="black", width=5)

img = Image.new("RGB", (W, H), "#0E1B2E")
d = ImageDraw.Draw(img)
# sunset band at top
for i in range(180):
    t = i / 180
    r = int(255 - 120 * t); g = int(120 - 40 * t); b = int(90 + 40 * t)
    d.line([(0, i), (W, i)], fill=(r, g, b))
# headline
text_center(d, 200, "MY 2013 PRE-ORDER", font(BOLD, 72), "white")
text_center(d, 280, "FINALLY ARRIVED", font(BOLD, 72), "#FFD166")

# receipt
rx0, ry0, rx1, ry1 = 80, 380, 700, 935
d.rectangle([rx0, ry0, rx1, ry1], fill="white", outline="#888888", width=3)
# zigzag bottom edge
for i in range(0, rx1 - rx0, 31):
    d.polygon([(rx0 + i, ry1), (rx0 + i + 15, ry1 + 18), (rx0 + i + 31, ry1)],
              fill="white", outline="#888888")
inner = rx0 + 28
d.text((inner, ry0 + 18), "VICE CITY GAMES", font=font(BOLD, 40), fill="black")
d.text((inner, ry0 + 66), "PRE-ORDER RECEIPT", font=font(BOLD, 30), fill="#333333")
d.line([(inner, ry0 + 112), (rx1 - 28, ry0 + 112)], fill="black", width=3)
lines = [
    ("DATE:", "17 SEP 2013"),
    ("ITEM:", "GRAND THEFT"),
    ("", "AUTO VI"),
    ("PRICE:", "$69.99"),
    ("STATUS:", "PAID IN FULL"),
]
yy = ry0 + 128
for k, v in lines:
    d.text((inner, yy), k, font=font(MONO, 30), fill="black")
    d.text((inner + 150, yy), v, font=font(MONO, 30), fill="black")
    yy += 40
d.line([(inner, yy + 6), (rx1 - 28, yy + 6)], fill="black", width=2)
yy += 22
d.text((inner, yy), "WAIT TIME: 13 YEARS", font=font(MONO, 30), fill="#C00000")
yy += 46
# red delivered stamp, rotated slightly via separate layer
stamp = Image.new("RGBA", (560, 110), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rectangle([4, 4, 556, 106], outline="#C00000", width=6)
sd.text((28, 28), "DELIVERED 19 NOV 2026", font=font(BOLD, 36), fill="#C00000")
stamp = stamp.rotate(-4, expand=True, resample=Image.BICUBIC)
img.paste(stamp, (inner - 6, yy + 18), stamp)
d = ImageDraw.Draw(img)

# ghost cashier, right of receipt, large and recognisable
draw_ghost(d, 730, 470, 270, 360)
d.text((728, 878), "the cashier", font=font(REG, 26), fill="#9FB3C8")
d.text((728, 910), "is still here too.", font=font(REG, 26), fill="#9FB3C8")

# bottom magenta make.fun banner
d.rectangle([0, 970, W, H], fill="#E5007E")
text_center(d, 992, "make.fun", font(BOLD, 64), "white")

img.save("/home/hatch/workspace/makefun/gta6-meme-x-01/gta6-meme.png")
# 480px preview check
small = img.copy()
small.thumbnail((480, 480))
small.save("/home/hatch/workspace/makefun/gta6-meme-x-01/gta6-meme-480.png")
print("saved 1080 and 480 preview")
