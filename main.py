import os
import re

def create_structure_from_txt(txt_path, base_dir="."):
    if not os.path.isfile(txt_path):
        print(f"File not found: {txt_path}")
        return

    with open(txt_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f if line.strip()]

    if not lines:
        print("The text file is empty!")
        return

    path_stack = []
    root_created = False

    for line in lines:
        if not root_created:
            root_name = line.rstrip("/")
            root_path = os.path.join(base_dir, root_name)
            os.makedirs(root_path, exist_ok=True)
            path_stack = [root_path]
            root_created = True
            continue

        level = line.count("│   ")

        name = re.sub(r"[│├└─ ]+", "", line)

        path_stack = path_stack[:level + 1]

        current_path = os.path.join(path_stack[-1], name)

        if name.endswith("/"):
            folder_path = current_path.rstrip("/")
            os.makedirs(folder_path, exist_ok=True)
            path_stack.append(folder_path)
        else:
            if "." in name:
                os.makedirs(os.path.dirname(current_path), exist_ok=True)
                open(current_path, "w").close()
            else:
                os.makedirs(current_path, exist_ok=True)
                path_stack.append(current_path)

    print(f"Root directory and structure created successfully from {txt_path}!")

if __name__ == "__main__":
    txt_file_path = input("Enter the path to your structure .txt file: ").strip()
    create_structure_from_txt(txt_file_path)
