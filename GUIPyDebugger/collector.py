import os
import shutil

def path_trimmer(file_paths, file_contents, folders):
    print(len(file_contents))
    print(len(file_paths))
    folder_prefix = os.path.commonpath(folders)
    file_prefix = os.path.commonpath(file_paths)
    # isolates the common base from paths such as ../../Project

    trimmed_folders, trimmed_files = [], []
    # create the trimmed path lists

    folder_prefix_len = len(folder_prefix)
    file_prefix_len = len(file_prefix)
    # get length of prefix, should make slicing faster

    for folder in folders:
        trimmed_folders.append(folder[folder_prefix_len+1:])

    for file in file_paths:
        trimmed_files.append(file[file_prefix_len+1:])
    # populate trimmed path lists
    
    return list(zip(trimmed_files, file_contents)), trimmed_folders

def create_folders(src_path, dest_path, folder_paths):
    os.makedirs(dest_path)   # recreate the destination path
    
    if len(folder_paths) == 0:
        len_original_src_path = len(src_path)
        src_path = src_path.lstrip("../")
        if len_original_src_path == len(src_path):
            src_path = src_path.lstrip("..\\")
        # sometimes the user will place a different seperator which powershell supports
        
        os.makedirs(os.path.join(dest_path, src_path))
        # when reading only files from dir, parent dir needs to be created

    for folder in folder_paths:
        print("Creating: ", folder)
        if not os.path.isdir(os.path.join(dest_path, folder)):
            os.makedirs(os.path.join(dest_path, folder))

def create_files(dest_path, file_tree_info):
    for file in file_tree_info:
        print("Creating: ", file[0])
        file_path = file[0]

        with open(os.path.join(dest_path, file_path), "w") as new_file:
            new_file.write(file[1])

def setup(dest_path):
    if os.path.isdir(dest_path):
        shutil.rmtree(dest_path) # remove the file tree recreation destination for repopulation

def read(file_path):
    contents = ""
    try:
        with open(file_path, "r") as file_contents:
            for line in file_contents.readlines():
                contents += line
        return contents
    except UnicodeDecodeError as e:
        return ""

def collector(path, file_paths = [], file_contents = [], folder_paths = []): #lists are instantiated on function definition
    results = os.listdir(path)
    for result in results:
        if result == os.path.basename(__file__):  #don't duplicate the file that is running the script
            continue    # not a problem if collector script isn't inside of the file tree being read
        relative_path = os.path.join(path, result)
        if os.path.isdir(relative_path):
            collector(relative_path)
            folder_paths.append(relative_path)
            # append folder paths to folder_paths
        else:
            file_content = read(os.path.join(path, result))
            file_paths.append(os.path.join(path, result))
            file_contents.append(file_content)
            # append file contents and file paths to respective lists

    return file_paths, file_contents, folder_paths

def main(src_path, dest_path):  
    if not os.path.isdir(src_path):
        print("[ERROR] Path Not Found: ", src_path)
        return False
    
    if ":" in src_path:
        print("[ERROR] Only relative paths are supported")
        return False

    file_paths, file_contents, folder_paths = collector(src_path)

    file_tree_info, folder_paths = path_trimmer(file_paths, file_contents, folder_paths)

    create_folders(src_path, dest_path, folder_paths)

    create_files(dest_path, file_tree_info)