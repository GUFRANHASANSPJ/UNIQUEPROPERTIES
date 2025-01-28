

# import os
# Function to find image and document files in the folder
# def get_files_in_directory(directory, extensions=("jpg", "jpeg", "png", "gif", "webp", "avif")):
#     # List to hold the paths of image/doc files
#     file_links = []

#     dirs = os.listdir(directory)

#     for dir in dirs:
#         dir_path = os.path.join(directory, dir)
#         for file in os.listdir(dir_path):
#             file_path = os.path.join(dir_path, file)
#             file_links.append(file_path.replace('\\','/'))

#         print(f"INSERT INTO tablename (file_path) VALUES ('{file_links}')")
#         file_links.clear()

#     return file_links


# Main logic
# if _name_ == "__main__":
#     folder_path = input("Enter the folder path to search for image/doc files: ")

    # Get image/document links from the folder
# folder_path = input("Enter the folder path to search for image/doc files: ")
# file_links = get_files_in_directory(folder_path)

# a='['/H:/pythonProject/media/media/properties_img/downtown-loft/1spanish-fort-town-center-spanish-fort-al.jpg/',
# '/H:/pythonProject/media/media/properties_img/downtown-loft/spanish-fort-town-center-spanish-fort-al-10.jpg/',  ]


# b= '[\"/media/properties_img/the-boulevard-bliss/1-general-canby-dr-spanish-fort-aljpg\",  \"/media/properties_img/the-boulevard-bliss/81-general-canby-dr-spanish-fort-al-2jpg\", ]'
import os

def create_folders(start, end, base_path):
    for i in range(start, end + 1):
        folder_name = f"p{i}"
        folder_path = os.path.join(base_path, folder_name)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"Folder created: {folder_path}")
        except Exception as e:
            print(f"Error creating folder {folder_name}: {e}")

# Specify the base path where folders will be created
folder_path = input("Enter the base path for folder creation: ").strip()

# Create folders p21 to p40 at the specified path
create_folders(1, 20, folder_path)
