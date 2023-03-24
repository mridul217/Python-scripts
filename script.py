import os
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Invert mask images.')
parser.add_argument('input_dir', type=str, help='input directory containing mask images')
parser.add_argument('output_dir', type=str, help='output directory for inverted mask images')
args = parser.parse_args()

# # Create output directory if it doesn't exist
# if not os.path.exists(args.output_dir):
#     os.makedirs(args.output_dir)

# Loop through mask images in input directory and invert them
# for filename in os.listdir(args.input_dir):
filename = args.input_dir
if filename.endswith('.png') or filename.endswith('.jpg'):
    # Open mask image
    # mask_path = os.path.join(args.input_dir, filename)
    mask_path=filename
    with Image.open(mask_path) as im:
        # Invert mask image
        inverted_im = im.convert('L').point(lambda x: 255 - x)

        # Save inverted mask image to output directory
        # output_path = os.path.join(args.output_dir, f"{filename}")
        output_path = args.output_dir
        inverted_im.save(output_path)
        print(f"Inverted mask image saved to {output_path}")

print("Done inverting mask images!")
