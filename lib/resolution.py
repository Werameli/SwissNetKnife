import shutil

def get_resolution():
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    return columns, lines