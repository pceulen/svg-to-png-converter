#!/usr/bin/env python3
"""
SVG to PNG Batch Converter
Converts all SVG files in a specified folder to PNG format.
"""

import os
import sys
from pathlib import Path
import argparse
import subprocess


def convert_svg_to_png_inkscape(svg_path, png_path, width=None, height=None):
    """
    Convert SVG to PNG using Inkscape command line.
    """
    cmd = ['inkscape', str(svg_path), '--export-type=png', f'--export-filename={str(png_path)}']
    
    if width:
        cmd.extend(['--export-width', str(width)])
    if height:
        cmd.extend(['--export-height', str(height)])
    
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        return False
    except FileNotFoundError:
        return None  # Inkscape not found


def convert_svg_to_png_rsvg(svg_path, png_path, width=None, height=None):
    """
    Convert SVG to PNG using rsvg-convert command line.
    """
    cmd = ['rsvg-convert', str(svg_path), '-o', str(png_path)]
    
    if width:
        cmd.extend(['-w', str(width)])
    if height:
        cmd.extend(['-h', str(height)])
    
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        return False
    except FileNotFoundError:
        return None  # rsvg-convert not found


def check_available_converters():
    """
    Check which SVG converters are available on the system.
    """
    converters = []
    
    # Check for Inkscape
    try:
        subprocess.run(['inkscape', '--version'], capture_output=True, check=True)
        converters.append('inkscape')
    except:
        pass
    
    # Check for rsvg-convert
    try:
        subprocess.run(['rsvg-convert', '--version'], capture_output=True, check=True)
        converters.append('rsvg-convert')
    except:
        pass
    
    return converters


def convert_svg_to_png(svg_path, png_path, width=None, height=None, scale=1, converter='auto'):
    """
    Convert a single SVG file to PNG using available converter.
    """
    # Apply scale to dimensions if provided
    if scale != 1:
        if width:
            width = int(width * scale)
        if height:
            height = int(height * scale)
    
    if converter == 'auto':
        # Try Inkscape first
        result = convert_svg_to_png_inkscape(svg_path, png_path, width, height)
        if result is True:
            return True
        elif result is False:
            print(f"Inkscape failed to convert {svg_path}")
        
        # Try rsvg-convert
        result = convert_svg_to_png_rsvg(svg_path, png_path, width, height)
        if result is True:
            return True
        elif result is False:
            print(f"rsvg-convert failed to convert {svg_path}")
            
    elif converter == 'inkscape':
        return convert_svg_to_png_inkscape(svg_path, png_path, width, height)
    elif converter == 'rsvg':
        return convert_svg_to_png_rsvg(svg_path, png_path, width, height)
    
    return False


def convert_folder(input_folder, output_folder=None, width=None, height=None, scale=1):
    """
    Convert all SVG files in a folder to PNG format.
    """
    # Check available converters
    available = check_available_converters()
    if not available:
        print("Error: No SVG converters found. Please install one of the following:")
        print("  - Inkscape: brew install inkscape")
        print("  - librsvg: brew install librsvg")
        return
    
    print(f"Available converters: {', '.join(available)}")
    
    input_path = Path(input_folder)
    
    if not input_path.exists():
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return
    
    if not input_path.is_dir():
        print(f"Error: '{input_folder}' is not a directory.")
        return
    
    # Set output folder
    if output_folder:
        output_path = Path(output_folder)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = input_path
    
    # Find all SVG files
    svg_files = list(input_path.glob("*.svg")) + list(input_path.glob("*.SVG"))
    
    if not svg_files:
        print(f"No SVG files found in '{input_folder}'.")
        return
    
    print(f"Found {len(svg_files)} SVG file(s) to convert...")
    
    # Convert each file
    success_count = 0
    for svg_file in svg_files:
        # Create output filename
        png_filename = svg_file.stem + ".png"
        png_path = output_path / png_filename
        
        print(f"Converting: {svg_file.name} -> {png_filename}")
        
        if convert_svg_to_png(svg_file, png_path, width, height, scale):
            success_count += 1
        else:
            print(f"  Failed to convert {svg_file.name}")
    
    print(f"\nConversion complete: {success_count}/{len(svg_files)} files converted successfully.")


def main():
    parser = argparse.ArgumentParser(description="Convert SVG files to PNG format")
    parser.add_argument("input_folder", help="Path to folder containing SVG files")
    parser.add_argument("-o", "--output", help="Output folder (defaults to input folder)")
    parser.add_argument("-w", "--width", type=int, help="Output width in pixels")
    parser.add_argument("--height", type=int, help="Output height in pixels")
    parser.add_argument("-s", "--scale", type=float, default=1, help="Scale factor (default: 1)")
    
    args = parser.parse_args()
    
    convert_folder(
        args.input_folder,
        args.output,
        args.width,
        args.height,
        args.scale
    )


if __name__ == "__main__":
    main()