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
            print(f"The location '{directory_path}' was found, continuing with the program \n\n")
            existing_path_given = True




    extensions = utils.check_extensions(directory_path)

    extensions = utils.remove_extensions_from_list(extensions)

    #print(extensions)

    if not extensions:
        print("The entered directory has no files in it")

    #print(extensions)

    categories = file_handler.extensions_to_categories(extensions)
    #print(categories)

    print("-----------------\n\n")
    print("You are about to make changes to this directory:")
    print(directory_path + "\n")
    print("Below are the extensions and categories that the files will be organized into: \n")
    print("     - File Extensions (file types inside the directory that will be organized): " + str(extensions) + "\n")
    print("     - Categories (folders the files will be organized into): " + str(categories) + "\n")

    print("Please make sure this is the correct directory where you want to make changes.")
    print("This action is not reversible. If you decide to revert, you will have to manually restore the previous state\n")
    
    validation = input("Are you sure you want to proceed? [Y/n]")

    if validation.casefold() == "y" or validation == "":

        file_handler.folder_create(categories=categories, directory_path=directory_path)
        file_handler.move_files_to_folders(directory_path=directory_path, extensions=extensions)

        print("Program successfully finished")

    else:
        print("Action cancelled, ending program")


if __name__ == "__main__":
    main()