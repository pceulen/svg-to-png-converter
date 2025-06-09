# SVG to PNG Batch Converter

A Python script that batch converts SVG files to PNG format using Inkscape or rsvg-convert.

## Features

- 🚀 Batch convert all SVG files in a folder
- 📁 Optional output folder specification
- 📐 Custom width/height settings
- 🔍 Scale factor support
- 🎯 Automatic converter detection (Inkscape or rsvg-convert)
- ✅ Progress feedback and error handling

## Prerequisites

You need at least one of the following SVG converters installed:

### Option 1: Inkscape (Recommended)
```bash
brew install inkscape
```

### Option 2: librsvg
```bash
brew install librsvg
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/svg-to-png-converter.git
cd svg-to-png-converter
```

2. Make sure you have Python 3.6+ installed:
```bash
python3 --version
```

3. (Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

### Basic Usage
Convert all SVG files in a folder (PNGs will be saved in the same folder):
```bash
python svg_to_png_converter.py /path/to/svg/folder
```

### Specify Output Folder
```bash
python svg_to_png_converter.py /path/to/svg/folder -o /path/to/output/folder
```

### Set Dimensions
```bash
# Set width (height will be proportional)
python svg_to_png_converter.py /path/to/svg/folder -w 1024

# Set height (width will be proportional)
python svg_to_png_converter.py /path/to/svg/folder --height 768

# Set both width and height
python svg_to_png_converter.py /path/to/svg/folder -w 1024 --height 768
```

### Scale Images
Double the size of all images:
```bash
python svg_to_png_converter.py /path/to/svg/folder -s 2
```

### Examples
```bash
# Convert SVGs in 'icons' folder to PNGs in 'icons-png' folder
python svg_to_png_converter.py ./icons -o ./icons-png

# Convert SVGs to 512x512 PNGs
python svg_to_png_converter.py ./logos -w 512 --height 512 -o ./logos-png

# Convert SVGs at 1.5x scale
python svg_to_png_converter.py ./graphics -s 1.5
```

## How It Works

The script:
1. Scans the input folder for all `.svg` and `.SVG` files
2. Checks for available converters (Inkscape or rsvg-convert)
3. Converts each SVG to PNG using the available converter
4. Saves PNGs with the same filename (different extension)
5. Reports progress and any errors

## Troubleshooting

### No converter found
If you see "No SVG converters found", install either Inkscape or librsvg:
```bash
# macOS
brew install inkscape
# or
brew install librsvg

# Ubuntu/Debian
sudo apt-get install inkscape
# or
sudo apt-get install librsvg2-bin

# Windows
# Download Inkscape from https://inkscape.org
```

### Permission errors
Make sure you have read permissions for the input folder and write permissions for the output folder.

### Conversion failures
Some complex SVGs might fail to convert. The script will report which files failed and continue with the rest.

## License

MIT License - feel free to use this in your projects!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---