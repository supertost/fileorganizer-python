import tempfile
import os
from application import file_handler
from application import utils


def test_folder_create():

    categories = ["Audio", "Image", "Video"]

    with tempfile.TemporaryDirectory() as temp_directory:

        file_handler.folder_create(categories=categories, directory_path=temp_directory)

        for category in categories:

            full_path = os.path.join(temp_directory, category)
            assert os.path.isdir(full_path), f"Folder '{category}' was not created"


def test_extensions_to_categories():

    extensions = ["mp3", "mp4", "ogg", "txt", "docx", "pptx", "blend"]

    categories = file_handler.extensions_to_categories(extensions=extensions)

    assert "Audio" in categories, "Audio not in categories"
    assert "Video" in categories, "Video not in categories"
    assert "Document" in categories, "Document not in categories"
    assert "blend" in categories, "Extension name from unknown category not in categories"


def test_categorize_by_type():

    file_mp3 = "file.mp3"
    category = file_handler.categorize_by_type(file_mp3)

    assert category == "Audio", "Audio category classification wrong"

    file_mp4 = "file.mp4"
    category = file_handler.categorize_by_type(file_mp4)

    assert category == "Video", "Video category classification wrong"

    file_txt = "file.txt"
    category = file_handler.categorize_by_type(file_txt)

    assert category == "Document", "Document category classification wrong"


def test_move_files_to_folders():

    categories = ["Audio", "Image", "Video", "Document"]
    
    with tempfile.TemporaryDirectory() as temp_directory:

        test_file = os.path.join(temp_directory, "test.txt")
        test_file2 = os.path.join(temp_directory, "test.png")
        test_file3 = os.path.join(temp_directory, "test.mp4")
        test_file4 = os.path.join(temp_directory, "test.mp3")
        test_file5 = os.path.join(temp_directory, "test.docx")

        for path in [test_file, test_file2, test_file3, test_file4, test_file5]:
            open(path, 'a').close()

        extensions = utils.check_extensions(temp_directory)

        file_handler.folder_create(categories=categories, directory_path=temp_directory)
        file_handler.move_files_to_folders(directory_path=temp_directory, extensions=extensions)

        full_path = os.path.join(temp_directory, "Document")
        full_path = os.path.join(full_path, "test.txt")
        assert os.path.isfile(full_path), "txt file not moved"

