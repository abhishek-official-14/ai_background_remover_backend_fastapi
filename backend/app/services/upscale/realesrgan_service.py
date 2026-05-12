from PIL import Image


class RealESRGANService:
    model_name = 'Real-ESRGAN'

    def upscale(self, input_path: str, scale: int = 2) -> Image.Image:
        img = Image.open(input_path).convert('RGBA')
        return img.resize((img.width * scale, img.height * scale), Image.Resampling.LANCZOS)
