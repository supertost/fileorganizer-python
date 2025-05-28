# File that handles the organization
import os
import shutil

def folder_create(extensions, directory_path):

    for extension in extensions:

        #extension = extension.replace(".", "")

        #print(extension)

        full_path = os.path.join(directory_path, extension)

        os.mkdir(full_path)

        print(f"Folder created at: {full_path}")



def move_files_to_folders(directory_path):
    
    for file in os.listdir(directory_path):

        full_path = os.path.join(directory_path, file)

        if os.path.isfile(full_path):

            filename, file_extension = os.path.splitext(file)
            file_extension = file_extension.replace(".", "")

            destination_directory = os.path.join(directory_path, file_extension)
            #print(destination_directory)

            shutil.move(full_path, destination_directory)

        