from PIL import Image
from rembg import remove


class RMBGService:
    model_name = 'RMBG-2.0'

    def process(self, input_path: str) -> Image.Image:
        img = Image.open(input_path).convert('RGBA')
        out = remove(img)
        return out if isinstance(out, Image.Image) else Image.open(out)
