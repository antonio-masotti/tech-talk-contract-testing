from PIL import Image

def resize_image(input_image_path, output_image_path, size = (296, 296)):
    """
    Resize the icons for the network graph

    :param input_image_path:
    :param output_image_path:
    :param size: tuple of (width, height) - default is (200, 200)
    :return:
    """
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)