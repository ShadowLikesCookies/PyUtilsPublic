import os

def del_file(file_path):
    try: os.remove(file_path)
    except FileNotFoundError: print(f"File '{file_path}' not found")