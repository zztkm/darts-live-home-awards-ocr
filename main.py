import re

from PIL import Image
import pyocr


engines = pyocr.get_available_tools()
engine = engines[0]

builder = pyocr.builders.TextBuilder(tesseract_layout=6)
txt = engine.image_to_string(Image.open("dl.png"), lang="eng", builder=builder)

ton80 = re.compile(r"TON 80 \d+")
nine_count = re.compile(r"9 COUNT \d+")

awards = [
        ton80,
        nine_count,
        ]

for line in txt.splitlines():
    if line == "":
        continue

    print(line)
    for award in awards:
        res = award.search(line)
        if res:
            print(res.group())
