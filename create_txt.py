import os
import glob

def generate_file_list_txt(input_folder, output_file):
    with open(output_file, "w") as file:
        # Use glob to directly filter files in the desired format
        files = glob.glob(os.path.join(input_folder, "*/*/[^0-9]*"), recursive=True)
        for file_path in files:
            relative_path = os.path.relpath(file_path, input_folder).replace(os.path.sep, '/')
            file.write(relative_path + "\n")

# Define the input folder and output file
input_folder = r"D:\video-interpolation-master\vimeo2_septuplet"  # Change this to your actual folder path
output_file = "tri.txt"  # You can change the filename or provide a full path

# Generate the file list text file
generate_file_list_txt(input_folder, output_file)

print(f"Text file '{output_file}' created successfully.")
