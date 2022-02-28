import pathlib
import shutil
import os

base_path = "C:/Users/Sandbox/Downloads/"
content = os.listdir(base_path)
folders = []


def sort_data(content: list, path: str):
    """Creates folders with the name of file extentions in ```path``` based on data in ```content```"""
    if not os.path.isdir(path + "sorted/"):
        os.mkdir(path + "sorted/")
    for file in content:
        if not os.path.isdir(path + file):
            extention = pathlib.Path(file).suffix.replace(".", "")
            if not os.path.isdir(path + "sorted/" + extention):
                os.mkdir(path + "sorted/" + extention)

            dst = path + "sorted/" + extention + "/" + file
            shutil.copyfile(path + file, dst)
    return


sort_data(content, base_path)
