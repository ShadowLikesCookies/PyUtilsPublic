import os

def create_init_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Check if __init__.py is already present
        if '__init__.py' not in filenames:
            # Create an empty __init__.py file
            init_path = os.path.join(dirpath, '__init__.py')
            open(init_path, 'w').close()
            print(f"Created __init__.py in {dirpath}")

if __name__ == "__main__":
    project_root = '/home/hugowoods/Desktop/pyutils'  # Replace with your project's root directory
    create_init_files(project_root)
