import os
import tempfile
from application import utils
from unittest.mock import patch


def test_check_extensions():

    with tempfile.TemporaryDirectory() as temp_directory:

        test_file = os.path.join(temp_directory, "test.txt")
        test_file2 = os.path.join(temp_directory, "test.png")
        test_file3 = os.path.join(temp_directory, "test.mp4")
        test_file4 = os.path.join(temp_directory, "test.mp3")
        test_file5 = os.path.join(temp_directory, "test.docx")

        for path in [test_file, test_file2, test_file3, test_file4, test_file5]:
            open(path, 'a').close()

        extensions = utils.check_extensions(temp_directory)

        assert "txt" in extensions, "txt not found in extensions"
        assert "png" in extensions, "png not found in extensions"
        assert "mp4" in extensions, "mp4 not found in extensions"
        assert "mp3" in extensions, "mp3 not found in extensions"
        assert "docx" in extensions, "docx not found in extensions"


def test_remove_extensions_from_list():

    extensions = ["mp4", "mp3", "ogg", "docx", "pptx", "txt", "csv"]

    with patch("builtins.input", return_value="mp4 ogg"):

        extensions = utils.remove_extensions_from_list(extensions=extensions)

        assert "mp4" not in extensions, "mp4 still in extensions"
        assert "ogg" not in extensions, "ogg still in extensions"

