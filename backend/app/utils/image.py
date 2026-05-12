from PIL import Image


def save_png(img: Image.Image, path: str) -> str:
    img.save(path, format='PNG')
    return path
