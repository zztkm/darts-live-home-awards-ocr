import re

from PIL import Image
import pyocr


engines = pyocr.get_available_tools()
engine = engines[0]

builder = pyocr.builders.TextBuilder(tesseract_layout=6)
txt = engine.image_to_string(Image.open("dl.png"), lang="eng", builder=builder)

ton80 = re.compile(r"TON 80 \d+")
high_ton = re.compile(r"HIGH TON \d+")
low_ton = re.compile(r"LOW TON \d+")
three_in_the_black = re.compile(r"3 IN THE BLACK \d+")
hat_trick = re.compile(r"HAT TRICK \d+")
three_in_a_bed = re.compile(r"3 IN A BED \d+")
white_horse = re.compile(r"WHITE HORSE \d+")
nine_count = re.compile(r"9 COUNT \d+")
eight_count = re.compile(r"8 COUNT \d+")
seven_count = re.compile(r"7 COUNT \d+")
six_count = re.compile(r"6 COUNT \d+")
five_count = re.compile(r"5 COUNT \d+")
d_bull = re.compile(r"D-BULL \d+")
s_bull = re.compile(r"S-BULL \d+")

awards = [
        ton80,
        high_ton,
        low_ton,
        three_in_the_black,
        hat_trick,
        three_in_a_bed,
        white_horse,
        nine_count,
        eight_count,
        seven_count,
        six_count,
        five_count,
        d_bull,
        s_bull
        ]

total_data = {}
for line in txt.splitlines():
    if line == "":
        continue

    match_count = 0
    for award in awards:
        res = award.search(line)
        if match_count == 2:
            break
        if res:
            text = res.group()
            splited = text.split(" ")
            num = splited[-1]
            name_list = splited[0:-1]
            name = " ".join(name_list)
            total_data[name] = num
            match_count += 1

print(total_data)
