import os
from PIL import Image

# Function to create a folder if it doesn't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to organize images into the specified format
def organize_images(input_folder, output_folder, group_size):
    subfolders = sorted([f for f in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, f))])

    for subfolder in subfolders:
        subfolder_path = os.path.join(input_folder, subfolder)
        output_subfolder_path = os.path.join(output_folder, "sequences", subfolder.zfill(5))

        create_folder(output_subfolder_path)

        image_files = sorted([f for f in os.listdir(subfolder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])

        folder_counter = 1
        for i in range(0, len(image_files), group_size):
            group = image_files[i:i + group_size]
            new_folder_name = str(folder_counter).zfill(4)
            new_folder_path = os.path.join(output_subfolder_path, new_folder_name)
            create_folder(new_folder_path)

            for img_file in group:
                img_path = os.path.join(subfolder_path, img_file)
                try:
                    img = Image.open(img_path)
                    img.save(os.path.join(new_folder_path, img_file))
                except Exception as e:
                    print(f"Error processing {img_file}: {e}")
            
            folder_counter += 1

# Define input and output folders
input_folder = r"D:\data_small"  # Change this to your actual Data folder path
output_folder = r"D:\vimeo2_septuplet"  # Change this to your desired output folder path

# Define the number of images to be grouped together
group_size = 3

# Organize the images into the specified format
organize_images(input_folder, output_folder, group_size)


