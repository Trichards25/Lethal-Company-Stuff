from PIL import Image, ImageOps
import os

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

    poster_dir = "./Output"
    tips_dir = "./Output"
    paintings_dir = "./Output"
    
    os.makedirs(poster_dir, exist_ok=True)
    os.makedirs(tips_dir, exist_ok=True)
    os.makedirs(paintings_dir, exist_ok=True)

    for i in range(len(p)):
        generate_atlas(
            poster_template,
            [
                g(p, i),
                g(p, i + 1),
                g(p, i + 2),
                g(p, i + 3),
                g(p, i + 4),
            ],
        ).save(f"{poster_dir}/{i+99}.png")

        generate_tips(g(p, i)).save(f"{tips_dir}/{i+99}.png")

        generate_painting(painting_template, g(p, i)).save(f"{paintings_dir}/{i+99}.png")

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
    print("Done!")
