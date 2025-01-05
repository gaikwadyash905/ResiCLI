# ResiCLI

ResiCLI is a powerful command-line tool designed to quickly and efficiently resize images in bulk. It supports various image formats and provides options for resizing, previewing, and specifying output directories.

## Features

- Bulk image resizing
- Support for various image formats (JPEG, PNG, etc.)
- Customizable output directory
- Preview resized images before saving
- Preserve aspect ratio option

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Install from Source

1. Clone the repository:

    ```bash
    git clone https://github.com/gaikwadyash905/ResiCLI.git
    cd ResiCLI
    ```

2. Install the package:

    ```bash
    python3 setup.py install
    ```

## Usage

### Basic Usage

To resize an image, use the following command:

```bash
resicli input_image.jpg --resize 800x600 --output /path/to/output_directory
```

### Options

--resize WIDTHxHEIGHT: Resize the image to the specified width and height.
--resize-by-percent PERCENTAGE: Resize the image by a specified percentage.
--output DIRECTORY: Specify the directory to save resized images. Default is the current working directory.
--preview: Preview the resized image before saving.
--preserve-aspect: Preserve the aspect ratio of the image.
--quality QUALITY: Set the quality of the output image (JPEG only). Default is 85%.
--undo: Restore original images from backup.

## Examples

1. Resize an image to 800x600 pixels and save it to the current directory:

    ```bash
    resicli input_image.jpg --resize 800x600
    ```

2. Resize an image to 800x600 pixels and save it to a specified directory:

    ```bash
    resicli input_image.jpg --resize 800x600 --output /path/to/output_directory
    ```

3. Preview the resized image before saving:

    ```bash
    resicli input_image.jpg --resize 800x600 --preview
    ```

4. Resize an image while preserving the aspect ratio:

    ```bash
    resicli input_image.jpg --resize 800x600 --preserve-aspect
    ```

5. Resize an image by 50% and save it to the current directory:

    ```bash
    resicli input_image.jpg --resize-by-percent 50
    ```

6. Restore the original image from backup:

    ```bash
    resicli input_image.jpg --undo
    ```

## Configuration

The configuration file `resicli_config.json` allows you to set default values for various options. Here is an example configuration file:

```json
{
  "default_output_dir": "resized_images",
  "default_resize_width": 800,
  "default_resize_height": 600,
  "preserve_aspect_ratio": true,
  "log_level": "INFO"
}
```

## Development

### Setting Up the Development Environment

1. Clone the repository:

    ```bash
    git clone https://github.com/gaikwadyash905/ResiCLI.git
    cd ResiCLI
    ```

2. Create a virtual environment:

    - For Windows

    ```bash
      python3 -m venv venv
      source venv\Scripts\activate
    ```

    - For Unix (Linux/MacOS)

    ```bash
      python3 -m venv venv
      source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.

For more details, see the [CONTRIBUTING](CONTRIBUTING.md) file.

License
This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

Contact
For any questions or suggestions, please contact Yash Gaikwad at <gaikwadyash905@gmail.com>.