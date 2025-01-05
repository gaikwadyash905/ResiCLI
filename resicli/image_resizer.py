from PIL import Image
import os
from resicli.config import DEFAULT_OUTPUT_DIR

def resize_image(image_path, width, height, preserve_aspect=False, output_dir="./output", quality=85):
    """
    Resize an image to the specified dimensions.
    """
    with Image.open(image_path) as img:
        if img.format not in ["JPEG", "PNG"]:
            raise ValueError(f"Unsupported image format: {img.format}")
        if preserve_aspect:
            img.thumbnail((width, height))
        else:
            img = img.resize((width, height))
        save_image(img, image_path, output_dir, quality)

def resize_by_percentage(image_path, percentage, output_dir="./output", quality=85):
    """
    Resize an image by a percentage.
    """
    with Image.open(image_path) as img:
        if img.format not in ["JPEG", "PNG"]:
            raise ValueError(f"Unsupported image format: {img.format}")
        new_width = int(img.width * (percentage / 100))
        new_height = int(img.height * (percentage / 100))
        img = img.resize((new_width, new_height))
        
        save_image(img, image_path, output_dir, quality)

def save_image(image, original_path, output_dir, quality=85):
    """
    Save the resized image to the specified output directory.
    """
    base_name = os.path.basename(original_path)
    output_path = os.path.join(output_dir, base_name)
    image.save(output_path, quality=quality)
    print(f"Saved resized image to {output_path}")

def preview_image(image_path, width, height, preserve_aspect=False):
    """
    Generate a resized preview of the image without saving it.
    """
    with Image.open(image_path) as img:
        if img.format not in ["JPEG", "PNG"]:
            raise ValueError(f"Unsupported image format: {img.format}")
        if preserve_aspect:
            img.thumbnail((width, height))
        else:
            img = img.resize((width, height))
        
        img.show()  # Opens the image in the default viewer for preview
        print("Preview displayed. Close the image viewer to continue.")

BACKUP_DIR = os.path.join(DEFAULT_OUTPUT_DIR, ".backup")

def backup_image(image_path):
    """
    Backup the original image before resizing.
    """
    os.makedirs(BACKUP_DIR, exist_ok=True)
    base_name = os.path.basename(image_path)
    backup_path = os.path.join(BACKUP_DIR, base_name)
    if not os.path.exists(backup_path):
        with open(image_path, 'rb') as original, open(backup_path, 'wb') as backup:
            backup.write(original.read())

def restore_image(image_path, output_dir="./output"):
    """
    Restore an image from the backup.
    """
    base_name = os.path.basename(image_path)
    backup_path = os.path.join(BACKUP_DIR, base_name)
    if os.path.exists(backup_path):
        output_path = os.path.join(output_dir, base_name)
        os.makedirs(output_dir, exist_ok=True)
        with open(backup_path, 'rb') as backup, open(output_path, 'wb') as restored:
            restored.write(backup.read())
        print(f"Restored {base_name} to {output_path}.")
    else:
        print(f"No backup found for {base_name}.")
