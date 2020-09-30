#
# This function identifies files (Can be different names) with identical contents within a folder
# TODO Modify to store hashes and identify duplicates in the entire file system

import hashlib, os, sys


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def is_folder(path):
    return os.path.isdir(path)


def list_folder(path):
    files_path = []
    for x in os.listdir(path):
        files_path.append(x)
    return files_path


result_dict = {}


def find_dupes(root_path):
    result_list = []
    file_dictionary = dict()
    local_temp_folder = list_folder(root_path)
    for my_file in local_temp_folder:
        explicit_path = root_path + "/" + my_file
        if is_folder(os.path.abspath(explicit_path)):
            find_dupes(explicit_path)
        else:
            hashcode = md5(explicit_path)
            file_list = []
            if hashcode not in file_dictionary:
                file_list.append(explicit_path)
                file_dictionary[hashcode] = file_list
            else:
                file_list = file_dictionary.get(hashcode)
                file_list.append(explicit_path)

    for key, value in file_dictionary.items():
        if len(value) > 1:
            for file in value:
                result_list.append(file)

            result_dict[root_path] = result_list
            return result_dict


if __name__ == "__main__":
    try:
        user_root_path = sys.argv[1]
    except Exception as e:
        print('WARNING: No path specificied, running in current path ')
        user_root_path = '.'

    try:
        my_results = find_dupes(user_root_path)
        if my_results:

            for entry, values in my_results.items():
                print('---------------------------------------------------------------------------------------------------------')
                print('Found Duplicate files named differently in this path: {}'.format(entry))
                for dup in values:
                    print('FILE: {}'.format(dup))

        else:
            print('NO DUPLICATE FILES FOUND!')
    except Exception as e:
        print('Cannot find records: ' + str(e))
