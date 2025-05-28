import os
from application import file_handler
from application import utils


def main():

    existing_path_given = False

    while (existing_path_given == False):   
        directory_path = input("Enter a directory to organize: ")

        if os.path.isfile(directory_path):
            print("The entered path is a file, please enter a folder path")
            continue

        if os.path.exists(directory_path):
            print(f"The location '{directory_path}' was found, continuing with the program")
            existing_path_given = True


    extensions = utils.check_extensions(directory_path)

    print(extensions)

    file_handler.folder_create(extensions=extensions, directory_path=directory_path)
    file_handler.move_files_to_folders(directory_path)




if __name__ == "__main__":
    main()