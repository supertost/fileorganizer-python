# File that handles the organization
import os
import shutil
import mimetypes

def folder_create(categories, directory_path):

    for category in categories:

        #extension = extension.replace(".", "")

        #print(extension)

        full_path = os.path.join(directory_path, category)

        os.mkdir(full_path)

        print(f"Folder created at: {full_path}")



def move_files_to_folders(directory_path, extensions):
    
    for file in os.listdir(directory_path):

        full_path = os.path.join(directory_path, file)

        if os.path.isfile(full_path):

            category = categorize_by_type(file)

            filename, file_extension = os.path.splitext(file)
            file_extension = file_extension.replace(".", "")
            
            if category == "Unknown":


                if file_extension in extensions:

                    destination_directory = os.path.join(directory_path, file_extension)
                    #print(destination_directory)
                    shutil.move(full_path, destination_directory)

            else:

                if file_extension in extensions:

                    destination_directory = os.path.join(directory_path, category)
                    #print(destination_directory)
                    shutil.move(full_path, destination_directory)



def extensions_to_categories(extensions):

    categories = set()

    for extension in extensions:

        category = categorize_by_type("file." + extension)

        if category == "Unknown":

            categories.add(extension)
        
        else:

            categories.add(categorize_by_type("file." + extension))

    #print(categories)

    return categories


def categorize_by_type(filename):

    mime, _ = mimetypes.guess_type(filename)

    if mime is None:
        return 'Unknown'
    
    if mime.startswith('audio/'):
        return 'Audio'
    
    if mime.startswith('video/'):
        return 'Video'
    
    if mime.startswith('image/'):
        return 'Image'
    
    if mime.startswith('application/') or mime.startswith('text/'):
        return 'Document'
    
    return 'Other'