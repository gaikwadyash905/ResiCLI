import argparse
from resicli.image_resizer import backup_image, preview_image, restore_image, resize_image
from resicli.utils import validate_files, create_output_dir
import os
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="ResiCLI: A Command-Line Image Resizer")
    
    # Positional argument for input images
    parser.add_argument(
        'images', 
        metavar='IMAGE', 
        type=str, 
        nargs='+', 
        help="List of image file paths to resize."
    )
    
    # Resize by pixel dimensions
    parser.add_argument(
        '--resize', 
        type=str, 
        help="Resize images to WIDTHxHEIGHT. Example: --resize 1024x768"
    )
    
    # Resize by percentage
    parser.add_argument(
        '--resize-by-percent', 
        type=int, 
        help="Resize images by a percentage. Example: --resize-by-percent 50"
    )
    
    # Preserve aspect ratio
    parser.add_argument(
        '--preserve-aspect', 
        action='store_true', 
        help="Maintain aspect ratio when resizing."
    )
    
    # Output directory
    parser.add_argument(
        '--output', 
        type=str, 
        default=os.getcwd(), 
        help="Directory to save resized images. Default: current working directory"
    )
    
    # Image quality
    parser.add_argument(
        '--quality', 
        type=int, 
        default=85, 
        help="Quality of output images (JPEG only). Default: 85"
    )
    
    # Preview option
    parser.add_argument(
        '--preview',
        action='store_true',
        help="Display a preview of the resized image without saving."
    )

    # Undo option
    parser.add_argument(
        '--undo',
        action='store_true',
        help="Restore original images from backup."
    )

    # Parse arguments
    args = parser.parse_args()
    
    # Validate input files
    valid_images = validate_files(args.images)
    if not valid_images:
        print("No valid image files provided. Exiting.")
        return

    # Validate resize format
    if args.resize and 'x' not in args.resize:
        print("Invalid format for --resize. Use WIDTHxHEIGHT format.")
        return
    
    # Create output directory
    create_output_dir(args.output)
    
    # Process each image
    for image_path in valid_images:
        try:
            print(f"Processing {image_path}...")
            backup_image(image_path)

            if args.resize:
                width, height = map(int, args.resize.split('x'))
                if args.preview:
                    preview_image(image_path, width, height, preserve_aspect=args.preserve_aspect)
                else:
                    resize_image(image_path, width, height, output_dir=args.output, preserve_aspect=args.preserve_aspect)
            elif args.resize_by_percent:
                with Image.open(image_path) as img:
                    new_width = int(img.width * (args.resize_by_percent / 100))
                    new_height = int(img.height * (args.resize_by_percent / 100))
                    if args.preview:
                        preview_image(image_path, new_width, new_height)
                    else:
                        resize_image(image_path, new_width, new_height, output_dir=args.output)
            else:
                print(f"Skipping {image_path}: No resizing option provided.")

        except Exception as e:
            print(f"Error processing {image_path}: {e}")

    print("Processing complete.")


if __name__ == "__main__":
    main()