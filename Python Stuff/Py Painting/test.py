import os
import argparse
from PIL import Image

# lastnum = 136
lastnum = 0


POSTER_OFFSETS = [
    (0, 0, 341, 559),
    (346, 0, 284, 559),
    (641, 58, 274, 243),
    (184, 620, 411, 364),
    (632, 320, 372, 672),
]

def main():
    parser = argparse.ArgumentParser(description="Generate posters, tips, and paintings.")
    parser.add_argument("output_type", choices=["posters", "tips", "paintings", "all"], help="Specify the type of output.")
    args = parser.parse_args()

    poster_template = Image.open("./posters_template.png")
    painting_template = Image.open("./painting_template.png")

    p = [Image.open(f.path) for f in os.scandir("./input") if f.is_file()]

    poster_dir = "./output/BepInEx/plugins/LethalPosters/posters"
    tips_dir = "./output/BepInEx/plugins/LethalPosters/tips"
    paintings_dir = "./output/BepInEx/plugins/LethalPaintings/paintings"
    
    
    os.makedirs(poster_dir, exist_ok=True)
    os.makedirs(tips_dir, exist_ok=True)
    os.makedirs(paintings_dir, exist_ok=True)

    for i in range(len(p)):
        if args.output_type in ["posters", "all"]:
            generate_atlas(
                poster_template,
                [
                    g(p, i),
                    g(p, i + 1),
                    g(p, i + 2),
                    g(p, i + 3),
                    g(p, i + 4),
                ],
            ).save(f"{poster_dir}/{i+lastnum}.png")

        if args.output_type in ["tips", "all"]:
            generate_tips(g(p, i)).save(f"{tips_dir}/{i+lastnum}.png")

        if args.output_type in ["paintings", "all"]:
            generate_painting(painting_template, g(p, i)).save(f"{paintings_dir}/{i+lastnum}.png")

def g(input_list, index):
    return input_list[index % len(input_list)]

def generate_atlas(template, posters):
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
    print("-"*20)
    print("Done!")
    print("-"*20)
