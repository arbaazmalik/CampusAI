import os


def ensure_directory(path: str):
    """
    Create the directory if it doesn't already exist.
    """
    os.makedirs(path, exist_ok=True)


def delete_file(file_path: str):
    """
    Delete a file if it exists.
    """
    if os.path.exists(file_path):
        os.remove(file_path)


def clear_directory(folder_path: str):
    """
    Delete all files inside a directory.
    """
    if not os.path.exists(folder_path):
        return

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if os.path.isfile(path):
            os.remove(path)