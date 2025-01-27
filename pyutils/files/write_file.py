import del_file
def write_file(file_path: str, data: any, mode: str):
    if isinstance(data, str):
        if mode == 'O':
            with open(file_path, 'w') as file:
                file.write(data)
        elif mode == 'N':
            with open(file_path, 'a') as file:
                file.write(data)
    elif isinstance(data, int):
        data = str(data)
        if mode == 'O':
            with open(file_path, 'w') as file:
                file.write(data)
        elif mode == 'N':
            with open(file_path, 'a') as file:
                file.write(data)
    elif isinstance(data, list):
        if all(isinstance(x, str) for x in data):
            if mode == 'O':
                with open(file_path, 'w') as file:
                    for i in data:
                        file.write(i)
            elif mode == 'N':
                with open(file_path, 'a') as file:
                    for i in data:
                        file.write(i)
        elif all(isinstance(x, int) for x in data):
            data = list(map(str, data))
            if mode == 'O':
                with open(file_path, 'w') as file:
                    for i in data:
                        file.write(i)
            elif mode == 'N':
                with open(file_path, 'a') as file:
                    for i in data:
                        file.write(i)
        else:
            raise TypeError("Type Error: Do not mix types in the array, Array must be of type int or of type str")


def run_tests():
    test_file = "test_output.txt"

    write_file(test_file, "Hello World", 'O')
    with open(test_file, 'r') as f:
        content = f.read()
    print("Test 1 - Write String Override:", content == "Hello World", "| Output:", content)

    write_file(test_file, "Hello", 'O')
    write_file(test_file, " World", 'N')
    with open(test_file, 'r') as f:
        content = f.read()
    print("Test 2 - Write String Next Line:", content == "Hello World", "| Output:", content)

    write_file(test_file, 12345, 'O')
    with open(test_file, 'r') as f:
        content = f.read()
    print("Test 3 - Write Integer Override:", content == "12345", "| Output:", content)

    write_file(test_file, 12345, 'O')
    write_file(test_file, 67890, 'N')
    with open(test_file, 'r') as f:
        content = f.read()
    print("Test 4 - Write Integer Next Line:", content == "1234567890", "| Output:", content)

    write_file(test_file, ["Hello", " ", "World"], 'O')
    with open(test_file, 'r') as f:
        content = f.read()
    print("Test 5 - Write List of Strings Override:", content == "Hello World", "| Output:", content)

    write_file(test_file, ["Hello"], 'O')
    write_file(test_file, [" ", "World"], 'N')
    with open(test_file, 'r') as f:
        content = f.read()
    print("Test 6 - Write List of Strings Next Line:", content == "Hello World", "| Output:", content)

    write_file(test_file, [1, 2, 3], 'O')
    with open(test_file, 'r') as f:
        content = f.read()
    print("Test 7 - Write List of Integers Override:", content == "123", "| Output:", content)

    write_file(test_file, [1], 'O')
    write_file(test_file, [2, 3], 'N')
    with open(test_file, 'r') as f:
        content = f.read()
    print("Test 8 - Write List of Integers Next Line:", content == "123", "| Output:", content)

    try:
        write_file(test_file, [1, "two", 3], 'O')
        print("Test 9 - Mixed Type List: Failed (No Exception Raised)")
    except TypeError as e:
        print("Test 9 - Mixed Type List: Passed | Exception:", str(e))

run_tests()

# Clean up test output file after tests

del_file.del_file("test_output.txt")