import os
import shutil
    
def create_folders(src_path, dest_path, folder_paths):
    os.makedirs(dest_path)   # recreate the destination path
    
    if len(folder_paths) == 0:
        p_dir_idx = src_path.rfind(".." + os.path.sep)
        if p_dir_idx == -1:
            p_dir_idx = src_path.rfind("../")
            # sometimes the user will place a different seperator which powershell supports
        
        folder_path = src_path[p_dir_idx + 3:]
        os.makedirs(os.path.join(dest_path, folder_path))
        # when reading only files from dir, that dir needs to be created

    for folder in folder_paths:
        print("Creating: ", folder)
        if not os.path.isdir(os.path.join(dest_path, folder)):
            os.makedirs(os.path.join(dest_path, folder))

def create_files(dest_path, file_tree_info):
    for file in file_tree_info:
        print("Creating: ", file[0])
        file_path = file[0]
        p_dir_idx = file_path.rfind(".." + os.path.sep)

        if p_dir_idx == -1:
            p_dir_idx = file_path.rfind("../")
            # sometimes the user will place a different seperator which powershell supports
        
        file_path = file[0][p_dir_idx + 3:]
        with open(os.path.join(dest_path, file_path), "w") as new_file:
            print(os.path.join(dest_path, file_path))
            new_file.write(file[1])

def setup(dest_path):
    if os.path.isdir(dest_path):
        shutil.rmtree(dest_path) # remove the file tree recreation destination

def read(file_path):
    contents = ""
    try:
        with open(file_path, "r") as file_contents:
            for line in file_contents.readlines():
                contents += line
        return contents
    except UnicodeDecodeError as e:
        return ""

def collector(path, file_tree_info = [], folder_paths = []): #file_tree_info is instantiated on function definition
    results = os.listdir(path)
    for result in results:
        if result == os.path.basename(__file__):  #don't duplicate the file that is running the script
            continue    # not a problem if collector script isn't inside of the file tree being read
        relative_path = os.path.join(path, result)
        if os.path.isdir(relative_path):
            collector(relative_path)
            folder_paths.append(relative_path)
        else:
            file_contents = read(os.path.join(path, result))
            file_tree_info.append((os.path.join(path, result), file_contents)) #(path, contents)

    return file_tree_info, folder_paths

def main(src_path, dest_path):  
    if not os.path.isdir(src_path):
        print("Path Not Found: ", src_path)
        return False

    file_tree_info, folder_paths = collector(src_path)

    create_folders(src_path, dest_path, folder_paths)

    create_files(dest_path, file_tree_info)