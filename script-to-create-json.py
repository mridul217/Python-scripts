import json
import os
import random

# Path to folder containing original images
orig_img_path = 'dataset/bike/kawasaki'

# Path to folder containing mask images
mask_img_path = 'dataset/bike/rembg-kawasaki'

# Path to file containing list of prompts
prompts_file_path = 'prompts.txt'

# Path to output JSON file
output_file = 'data.json'

# List of prompts read from file
with open(prompts_file_path, 'r') as f:
    prompts = [line.strip() for line in f]

# Read all original image filenames in the folder
orig_img_filenames = [filename for filename in os.listdir(orig_img_path) if filename.endswith('.jpg') or filename.endswith('.png')]

# Shuffle the original image filenames randomly
random.shuffle(orig_img_filenames)

# Create an empty list to store the JSON objects
json_data_list = []

# Loop over each original image and append the JSON data to the output file
for i, orig_img_filename in enumerate(orig_img_filenames):
    # Choose a random prompt from the list of prompts
    prompt = random.choice(prompts)

    # Generate a random seed
    seed = random.randint(1, 100000)

    # Construct the JSON object
    json_data = {
        'path_original_image': os.path.join(orig_img_path, orig_img_filename),
        'path_mask_image': os.path.join(mask_img_path, f'mask_{i}.jpg'),
        'seed': seed,
        'prompt': prompt
    }

    # Append the JSON object to the list
    json_data_list.append(json_data)

# Write the list of JSON objects to the output file
with open(output_file, 'a') as f:
    json.dump(json_data_list, f, indent=2)
    f.write('\n')