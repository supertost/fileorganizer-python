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