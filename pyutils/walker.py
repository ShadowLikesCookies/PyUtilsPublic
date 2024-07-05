import os

def generate_project_structure(root_dir, indent=''):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            print(f"{indent}📁 {item}/")
            generate_project_structure(item_path, indent + '    ')
        else:
            print(f"{indent}📄 {item}")

if __name__ == "__main__":
    project_root = '/home/hugowoods/Desktop/pyutils'  # Replace with your project's root directory
    print(f"Project structure of '{project_root}':")
    generate_project_structure(project_root)
