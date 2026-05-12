from PIL import Image, ImageEnhance


class MODNetService:
    model_name = 'MODNet'

    def refine_hair(self, image: Image.Image) -> Image.Image:
        return ImageEnhance.Sharpness(image).enhance(1.2)
