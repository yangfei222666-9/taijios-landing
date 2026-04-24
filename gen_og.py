"""Generate the TaijiOS social preview image.

The image must match the current positioning:
failure visibility, event flow, degraded gates, and experience pool.
It intentionally avoids old claims about prediction accuracy or persona lore.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


W, H = 1200, 630
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "og.png"


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/SFNSMono.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size, index=0)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    lines: list[str],
    fnt: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    gap: int,
) -> int:
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        bbox = draw.textbbox((x, y), line, font=fnt)
        y = bbox[3] + gap
    return y


img = Image.new("RGB", (W, H), (244, 239, 228))

glow = Image.new("RGB", (W, H), (244, 239, 228))
gd = ImageDraw.Draw(glow)
gd.ellipse([-120, -140, 560, 520], fill=(199, 52, 34))
gd.ellipse([700, -90, 1320, 500], fill=(17, 111, 102))
gd.ellipse([420, 360, 1080, 790], fill=(196, 146, 46))
glow = glow.filter(ImageFilter.GaussianBlur(105))
img = Image.blend(img, glow, 0.22)

draw = ImageDraw.Draw(img)

# Background grid and grain.
for x in range(0, W, 56):
    draw.line([(x, 0), (x, H)], fill=(224, 213, 195), width=1)
for y in range(0, H, 56):
    draw.line([(0, y), (W, y)], fill=(224, 213, 195), width=1)

# Right-side dark system card.
card = [760, 82, 1128, 548]
draw.rounded_rectangle(card, radius=34, fill=(19, 16, 13), outline=(56, 46, 37), width=2)
draw.text((802, 126), "RUN STATUS", font=font(22), fill=(196, 146, 46))
rows = [
    ("preflight", "ok"),
    ("event_flow", "recorded"),
    ("learning", "degraded"),
    ("judgment", "blocked"),
]
y = 182
for key, value in rows:
    fill = (255, 248, 233) if value != "blocked" else (241, 110, 85)
    draw.rounded_rectangle([802, y, 1086, y + 58], radius=16, fill=(38, 31, 25))
    draw.text((824, y + 16), key, font=font(20), fill=(166, 154, 137))
    draw.text((956, y + 16), value, font=font(20), fill=fill)
    y += 76

# Minimal Taiji mark.
cx, cy, r = 1032, 492, 38
outer = [cx - r, cy - r, cx + r, cy + r]
draw.ellipse(outer, fill=(255, 248, 233), outline=(199, 52, 34), width=3)
draw.pieslice(outer, 90, 270, fill=(19, 16, 13))
draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy], fill=(19, 16, 13))
draw.ellipse([cx - r // 2, cy, cx + r // 2, cy + r], fill=(255, 248, 233))
draw.ellipse([cx - 8, cy - r // 2 - 8, cx + 8, cy - r // 2 + 8], fill=(255, 248, 233))
draw.ellipse([cx - 8, cy + r // 2 - 8, cx + 8, cy + r // 2 + 8], fill=(19, 16, 13))

# Left copy.
draw.rounded_rectangle([58, 78, 352, 122], radius=22, fill=(255, 249, 235), outline=(224, 213, 195))
draw.text((82, 90), "TAIJIOS · AI OPS LAYER", font=font(20), fill=(199, 52, 34))

draw_multiline(
    draw,
    (58, 158),
    ["失败会主动报警。", "把假成功拦在门外。"],
    font(62, bold=True),
    (21, 17, 13),
    10,
)

draw.rectangle([62, 326, 244, 332], fill=(199, 52, 34))

draw_multiline(
    draw,
    (60, 362),
    [
        "预检 · 事件流 · 降级模式 · 经验池",
        "让智能代理工作流可检查、可恢复、可复盘",
    ],
    font(31),
    (72, 62, 51),
    14,
)

pill_y = 510
for text, color, x in [
    ("ok", (17, 111, 102), 60),
    ("degraded = learning_only", (196, 146, 46), 138),
    ("failed = loud report", (199, 52, 34), 488),
]:
    w = draw.textbbox((0, 0), text, font=font(22))[2] + 34
    draw.rounded_rectangle([x, pill_y, x + w, pill_y + 46], radius=23, fill=color)
    draw.text((x + 17, pill_y + 11), text, font=font(22), fill=(255, 248, 233))

draw.text((60, 582), "taijios.xyz", font=font(28), fill=(21, 17, 13))

img.save(OUT, "PNG", optimize=True)
print(f"saved {OUT} · {W}x{H} · {OUT.stat().st_size / 1024:.1f} KB")
