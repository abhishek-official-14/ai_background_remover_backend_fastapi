from PIL import Image, ImageFilter


class BiRefNetService:
    model_name = 'BiRefNet'

    def refine(self, image: Image.Image) -> Image.Image:
        return image.filter(ImageFilter.SMOOTH_MORE)
