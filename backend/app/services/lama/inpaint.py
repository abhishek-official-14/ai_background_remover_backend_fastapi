from PIL import Image


class LaMaInpaintService:
    model_name = 'LaMa'

    def inpaint(self, input_path: str) -> Image.Image:
        return Image.open(input_path).convert('RGBA')
