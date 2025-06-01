import random
import matplotlib.pyplot as plt

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xffffff))

def generate_palette(n=5):
    return [generate_random_color() for _ in range(n)]

def diplay_palette(palette):
    fig, ax = plt.subplots(figsize=(8, 2))
    for i, color in enumerate(palette):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
    ax.set_xlim(0, len(palette))
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    palette = generate_palette(5)
    print("Generated Color Palette:", palette)
    diplay_palette(palette)    