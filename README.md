# Image Color Inverter

This Python script allows you to invert the colors of an image file. It utilizes the Pillow (PIL) library for image manipulation and a graphical user interface (GUI) for selecting the input image file.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Techniques Used](#techniques-used)
- [Libraries Used](#libraries-used)
- [Algorithm](#algorithm)
- [File Naming](#file-naming)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To use this script, follow the steps below:

1. Clone this repository to your local machine or download the script directly.
2. Ensure you have the necessary prerequisites.
3. Run the script and select the image file you want to invert.
4. The inverted image will be saved with a unique name to avoid overwriting the original.
Let's try with this 10k resolution image:

 Before:
   
![Imagem normal](2188850.jpg)

After:

![Imagem Invertida](imagem_invertida_3.jpeg)


## Prerequisites

Before using the script, you need to have the following:

- Python 3 installed on your machine.
- Pillow (PIL) library installed. You can install it using `pip install Pillow`.

## Usage

1. Run the script by executing `python image_color_inverter.py`.
2. A file dialog will appear, allowing you to select an image file (JPEG, PNG, GIF, etc.).
3. The script will invert the colors of the selected image.
4. The inverted image will be saved in the same directory with a unique name.

## Techniques Used

The following techniques are applied in this script:

- **Image Processing**: The Pillow (PIL) library is used for image loading, manipulation, and saving.

## Libraries Used

This script relies on the following Python library:

- **Pillow (PIL)**: Used for image manipulation.

## Algorithm

The color inversion is achieved by iterating through each pixel of the image and calculating the new pixel color as follows:

```python
new_pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
```

This calculates the inverse of the red, green, and blue (RGB) components of each pixel, resulting in an inverted color.

## File Naming

To prevent overwriting existing files, the script generates a unique filename for the inverted image. It appends an incrementing number to the base filename until a unique filename is found.

## Contributing

Contributions to this project are welcome. Feel free to open issues or pull requests to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
