from PIL import Image


class SAM2Predictor:
    model_name = 'SAM2'

    def segment(self, input_path: str) -> Image.Image:
        return Image.open(input_path).convert('RGBA')
