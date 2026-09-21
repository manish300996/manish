#!/usr/bin/env python3
"""LinkedIn-ready infographic images for a general Data Engineering post."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
NAVY = (14, 39, 68)
NAVY2 = (19, 48, 82)
INK = (27, 36, 48)
MUTED = (90, 100, 115)
GOLD = (184, 137, 45)
TEAL = (15, 110, 107)
CREAM = (251, 250, 246)
WHITE = (255, 255, 255)
RED = (139, 46, 46)
OK = (15, 110, 107)

FONT = "/usr/share/fonts/truetype/macos/Inter-Regular.ttf"
FONT_M = "/usr/share/fonts/truetype/macos/Inter-Medium.ttf"
FONT_B = "/usr/share/fonts/truetype/macos/Inter-Bold.ttf"
FONT_SB = "/usr/share/fonts/truetype/macos/Inter-SemiBold.ttf"


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def rounded(draw, xy, r, fill):
    draw.rounded_rectangle(xy, radius=r, fill=fill)


def header_bar(img, title, kicker):
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, img.width, 168), fill=NAVY)
    d.rectangle((56, 148, 200, 152), fill=GOLD)
    d.text((56, 36), kicker, font=fnt(FONT_SB, 22), fill=GOLD)
    d.text((56, 72), title, font=fnt(FONT_B, 42), fill=WHITE)
    return d


def footer(d, w, h, note="Data Engineering  ·  production fundamentals"):
    d.rectangle((0, h - 72, w, h), fill=NAVY)
    d.text((56, h - 48), note, font=fnt(FONT_M, 20), fill=(215, 201, 164))


def img1_six_boxes():
    W, H = 1080, 1350
    im = Image.new("RGB", (W, H), CREAM)
    d = header_bar(im, "Data Engineering\nin 6 boxes.", "FRAMEWORK")
    # header is 168, title two lines - actually I used one line title that wraps visually
    # redraw header taller for 2-line title
    d.rectangle((0, 0, W, 220), fill=NAVY)
    d.text((56, 36), "A CLEAN FRAMEWORK", font=fnt(FONT_SB, 20), fill=GOLD)
    d.text((56, 78), "Data Engineering", font=fnt(FONT_B, 48), fill=WHITE)
    d.text((56, 138), "in 6 boxes.", font=fnt(FONT_B, 48), fill=(215, 201, 164))
    d.rectangle((56, 198, 180, 202), fill=GOLD)

    boxes = [
        ("01", "GRAIN", "One row = one meaning.\nWrong grain → every\ndashboard looks buggy."),
        ("02", "INCREMENTAL", "unique_key + lookback\n+ MERGE. Full refresh\nis not a strategy."),
        ("03", "BATCH vs CDC", "8am SLA → batch.\nChange-as-it-happens\n→ stream. Tool ≠ reason."),
        ("04", "ORCHESTRATION", "Retries. SLA.\nIdempotent. Backfill.\nReplay = production."),
        ("05", "TESTS → GOLD", "unique · not_null\n· relationships.\nBad keys never publish."),
        ("06", "TUNE FIRST", "Partitions · file size\n· shuffle vs broadcast.\nSpark UI before scale."),
    ]
    cols, rows = 2, 3
    gap, left, top = 22, 48, 240
    bw = (W - left * 2 - gap) // 2
    bh = 300
    for i, (num, title, body) in enumerate(boxes):
        r, c = divmod(i, cols)
        x = left + c * (bw + gap)
        y = top + r * (bh + gap)
        rounded(d, (x, y, x + bw, y + bh), 22, WHITE)
        d.rectangle((x, y, x + 10, y + bh), fill=TEAL if i % 2 == 0 else GOLD)
        d.text((x + 28, y + 22), num, font=fnt(FONT_B, 22), fill=GOLD)
        d.text((x + 28, y + 56), title, font=fnt(FONT_B, 26), fill=NAVY)
        yy = y + 108
        for line in body.split("\n"):
            d.text((x + 28, yy), line, font=fnt(FONT_M, 20), fill=MUTED)
            yy += 32
    footer(d, W, H, "SQL  ·  Python  ·  Spark  ·  dbt  ·  Airflow  ·  CDC  ·  DQ")
    p = OUT / "01_six_boxes.png"
    im.save(p, "PNG", optimize=True)
    return p


def img2_list():
    W, H = 1080, 1350
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 220), fill=NAVY)
    d.text((56, 40), "THE UNGLAMOROUS HALF", font=fnt(FONT_SB, 20), fill=GOLD)
    d.text((56, 82), "What the job\nactually is.", font=fnt(FONT_B, 48), fill=WHITE)

    items = [
        ("01", "Model the grain", "One row, one meaning. Tools cannot fix this."),
        ("02", "Load incrementally", "MERGE with a key and a lookback window."),
        ("03", "Choose batch or CDC", "On purpose — not because the JD lists Kafka."),
        ("04", "Make the DAG replayable", "Retries, SLA, idempotent tasks, backfill."),
        ("05", "Test before gold", "unique / not_null / relationships — or it is a dump."),
        ("06", "Read Spark UI first", "Then file size and shuffle. Cluster last."),
    ]
    y = 252
    for num, title, sub in items:
        rounded(d, (48, y, W - 48, y + 132), 18, WHITE)
        d.ellipse((72, y + 38, 128, y + 94), fill=NAVY)
        tw = d.textlength(num, font=fnt(FONT_B, 20))
        d.text((100 - tw / 2, y + 52), num, font=fnt(FONT_B, 20), fill=GOLD)
        d.text((156, y + 32), title, font=fnt(FONT_B, 28), fill=NAVY)
        d.text((156, y + 74), sub, font=fnt(FONT_M, 20), fill=MUTED)
        y += 148
    footer(d, W, H, "SQL + Python + Spark still do 80% of the job.")
    p = OUT / "02_unglamorous_half.png"
    im.save(p, "PNG", optimize=True)
    return p


def img3_before_after():
    W, H = 1080, 1350
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 200), fill=NAVY)
    d.text((56, 36), "LOOKS LIKE  vs  ACTUALLY IS", font=fnt(FONT_SB, 20), fill=GOLD)
    d.text((56, 78), "Tools vs discipline.", font=fnt(FONT_B, 44), fill=WHITE)
    d.text((56, 140), "Same role. Different bar.", font=fnt(FONT_M, 22), fill=(201, 211, 224))

    pairs = [
        ("Pipeline ran", "Same number tomorrow\nafter late data"),
        ("Full refresh\nevery night", "MERGE with a key\nand a lookback"),
        ("New cluster", "Smaller files,\nless shuffle"),
        ("More dashboards", "Tests on gold"),
    ]
    y = 232
    for left, right in pairs:
        rounded(d, (48, y, 516, y + 200), 20, WHITE)
        rounded(d, (564, y, 1032, y + 200), 20, WHITE)
        d.rectangle((48, y, 58, y + 200), fill=RED)
        d.rectangle((564, y, 574, y + 200), fill=OK)
        d.text((80, y + 22), "LOOKS LIKE", font=fnt(FONT_SB, 16), fill=RED)
        d.text((596, y + 22), "ACTUALLY IS", font=fnt(FONT_SB, 16), fill=OK)
        ly = y + 58
        for line in left.split("\n"):
            d.text((80, ly), line, font=fnt(FONT_B, 26), fill=NAVY)
            ly += 36
        ry = y + 58
        for line in right.split("\n"):
            d.text((596, ry), line, font=fnt(FONT_B, 26), fill=NAVY)
            ry += 36
        y += 220
    footer(d, W, H, "Tools change.  Grain, incremental, replay, quality do not.")
    p = OUT / "03_looks_like_vs_is.png"
    im.save(p, "PNG", optimize=True)
    return p


def img_square_cover():
    W, H = 1080, 1080
    im = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(im)
    d.rectangle((56, 72, 200, 78), fill=GOLD)
    d.text((56, 110), "DATA ENGINEERING", font=fnt(FONT_SB, 24), fill=GOLD)
    d.text((56, 170), "Not more tools.", font=fnt(FONT_B, 64), fill=WHITE)
    d.text((56, 250), "Better contracts.", font=fnt(FONT_B, 64), fill=(215, 201, 164))
    lines = [
        "Grain  ·  Incremental  ·  Batch vs CDC",
        "Replayable DAGs  ·  Tests before gold",
        "Spark UI before a bigger cluster",
    ]
    y = 400
    for line in lines:
        rounded(d, (56, y, 1024, y + 88), 16, NAVY2)
        d.text((88, y + 26), line, font=fnt(FONT_M, 26), fill=WHITE)
        y += 108
    d.text((56, 980), "SQL  ·  Python  ·  Spark  ·  dbt  ·  Airflow  ·  CDC", font=fnt(FONT_M, 22), fill=GOLD)
    p = OUT / "00_cover_square.png"
    im.save(p, "PNG", optimize=True)
    return p


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    paths = [img_square_cover(), img1_six_boxes(), img2_list(), img3_before_after()]
    for p in paths:
        print(p, Image.open(p).size)


if __name__ == "__main__":
    main()
