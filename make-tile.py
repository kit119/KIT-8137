import os
import glob
from PIL import Image
COLS, ROWS = 6, 3
PER_PAGE = COLS * ROWS
TARGET_W, TARGET_H = 8640, 5760
CELL_W, CELL_H = TARGET_W // COLS, TARGET_H // ROWS
def make_tile():
    images_path = sorted(glob.glob("*.jpg"))
    if not images_path:
        print("No JPG files found!")
        return
    pages = [images_path[i:i+PER_PAGE] for i in range(0, len(images_path), PER_PAGE)]
    for idx, group in enumerate(pages, 1):
        canvas = Image.new("RGB", (TARGET_W, TARGET_H), (255, 255, 255))
        for i, img_path in enumerate(group):
            with Image.open(img_path) as img:
                img = img.convert("RGB")
                ratio = min(CELL_W / img.width, CELL_H / img.height)
                nw, nh = int(img.width * ratio), int(img.height * ratio)
                resized = img.resize((nw, nh), Image.LANCZOS)
                r, c = i // COLS, i % COLS
                x = c * CELL_W + (CELL_W - nw) // 2
                y = r * CELL_H + (CELL_H - nh) // 2
                canvas.paste(resized, (x, y))
        output_name = f"result_{idx:03d}.jpg"
        canvas.save(output_name, "JPEG", quality=85)
        print(f"Saved: {output_name}")
if __name__ == "__main__":
    make_tile()