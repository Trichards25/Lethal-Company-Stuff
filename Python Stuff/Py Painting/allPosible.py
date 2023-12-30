import os
from itertools import combinations
from PIL import Image

lastnum = 0

POSTER_OFFSETS = [
    (0, 0, 341, 559),
    (346, 0, 284, 559),
    (641, 58, 274, 243),
    (184, 620, 411, 364),
    (632, 320, 372, 672),
]

def main():
    poster_template = Image.open("./posters_template.png")
    painting_template = Image.open("./painting_template.png")

    p = [Image.open(f.path) for f in os.scandir("./input") if f.is_file()]

    poster_dir = "./output/BepInEx/plugins/LethalPosters/posters"
    tips_dir = "./output/BepInEx/plugins/LethalPosters/tips"
    paintings_dir = "./output/BepInEx/plugins/LethalPaintings/paintings"

    os.makedirs(poster_dir, exist_ok=True)
    os.makedirs(tips_dir, exist_ok=True)
    os.makedirs(paintings_dir, exist_ok=True)

    for combo in combinations(p, 5):  # Choose 5 pictures for each poster
        generate_posters(poster_template, combo).save(f"{poster_dir}/{lastnum}.png")
        generate_tips(list(combo)[0]).save(f"{tips_dir}/{lastnum}.png")
        generate_painting(painting_template, list(combo)[0]).save(f"{paintings_dir}/{lastnum}.png")
        lastnum += 1

    print("-"*20)
    print("Done!")
    print("-"*20)

def generate_posters(template, posters):
    base = template.copy()
    for i, o in enumerate(POSTER_OFFSETS):
        p = posters[i].resize((o[2], o[3]), Image.LANCZOS)
        base.paste(p, ((o[0] + o[2] - p.width), o[1]))
    return base

def generate_tips(poster):
    base = Image.new("RGBA", (796, 1024))
    p = poster.resize((796, 1024), Image.LANCZOS)
    base.paste(p, (796 - p.width, 0))
    return base

def generate_painting(template, poster):
    base = template.copy()
    p = poster.resize((243, 324), Image.LANCZOS)
    base.paste(p, (264, 19))
    return base

if __name__ == "__main__":
    main()
