# File that handles the metadata and file extension check
import os

def check_extensions(directory_path):

    extensions = set()

    for file in os.listdir(directory_path):

        full_path = os.path.join(directory_path, file)

        if os.path.isfile(full_path):

            filename, file_extension = os.path.splitext(file)
            #print(f"File extension: {file_extension}")

            file_extension = file_extension.replace(".", "")

            extensions.add(file_extension)


    return extensions


def remove_extensions_from_list(extensions):
    
    print(extensions)
    print()

    print("The above are the file extensions present in the specified directory.")
    print("Enter the extensions you want to remove from the list (for example: mp3 mp4 ogg).")
    print("Press enter without typing anything if you do not want to remove any extensions.")

    extensions_to_remove = input()
    extensions_to_remove_array = extensions_to_remove.split()

    for extension in extensions_to_remove_array:
        if extension in extensions:
            extensions.remove(extension)

    return extensions
