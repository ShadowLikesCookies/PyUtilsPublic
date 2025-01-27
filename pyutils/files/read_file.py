
# Expected current modes. Whole string, Or Per Line Array
#Expects mode = 's' for whole string or mode = 'l' for lined array
def read_file(file_path: str, mode : str):
    array = []
    file = open(file_path, 'r')
    if mode == "s": return file.read()
    if mode == "l": 
        for line in file:
             array.append(line.strip())
        return array
        
