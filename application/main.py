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

    extensions = utils.remove_extensions_from_list(extensions)

    #print(extensions)

    if not extensions:
        print("The entered directory has no files in it")

    #print(extensions)

    categories = file_handler.extensions_to_categories(extensions)
    #print(categories)

    print("-----------------\n\n")
    print("You are about to make changes in this directory:")
    print(directory_path + "\n")
    print("Below are the extensions and categories that the files are going to organized in \n")
    print("extensions (file types inside the directory): " + str(extensions) + "\n")
    print("categories (folders the files are going to be organized in): " + str(categories) + "\n")

    print("Make sure this is the correct directory that you want to make changes to")
    print("This action is not reversible, if you decide to revert back, you have to manually revert it back to the previous state if you do this\n")
    
    validation = input("Are you sure you want to proceed? [Y/n]")

    if validation.casefold() == "y" or validation == "":

        file_handler.folder_create(categories=categories, directory_path=directory_path)
        file_handler.move_files_to_folders(directory_path=directory_path, extensions=extensions)

        print("Program successfully finished")

    else:
        print("Action cancelled, ending program")


if __name__ == "__main__":
    main()