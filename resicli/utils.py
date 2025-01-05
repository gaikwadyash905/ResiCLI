import os
from PIL import Image
from resicli.config import DEFAULT_OUTPUT_DIR

def validate_files(file_paths):
    """
    Validate a list of file paths, ensuring they exist and are valid image formats.
    """
    valid_files = []
    for file_path in file_paths:
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    valid_files.append(file_path)
            except Exception:
                print(f"Invalid or unsupported image file: {file_path}")
        else:
            print(f"File not found: {file_path}")
    return valid_files

def create_output_dir(output_dir):
    """
    Create the output directory if it doesn't exist.
    """
    output_dir = output_dir or DEFAULT_OUTPUT_DIR
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

def resize_image(image_path, output_path, size):
    """
    Resize the image to the specified size and save it to the output path.

    :param image_path: Path to the input image.
    :param output_path: Path to save the resized image.
    :param size: Tuple (width, height) specifying the new size.
    """
    try:
        with Image.open(image_path) as img:
            resized_img = img.resize(size, Image.ANTIALIAS)
            resized_img.save(output_path)
            print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")
