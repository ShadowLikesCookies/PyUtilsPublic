
def new_file(file_path: str):
    try:
        with open(file_path, 'x') as file:
            pass
    except Exception as e:
        print(f"An unknown error has occured: {e}")