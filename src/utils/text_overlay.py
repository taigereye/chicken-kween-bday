# Utility functions for adding text overlays to images

from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image, text, position=(10, 10)):
    """
    Add a text overlay to the given image.
    Arguments:
        image: A PIL.Image object.
        text: The text to overlay on the image.
        position: Tuple (x, y) for the text position.
    Returns:
        A PIL.Image object with the text overlay.
    """
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # Use default font
    draw.text(position, text, fill="black", font=font)
    return image
