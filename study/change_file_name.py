# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import os
import glob


def parse_argument():
    DEFAULT_SOURCE = ''

    parser = argparse.ArgumentParser(description='add index to file')

    parser.add_argument('--dir', action="store", dest="source", default=DEFAULT_SOURCE)

    given_args = parser.parse_args()

    try:
        source_dir = given_args.source
    except Exception as e:
        print(f'Exception: {e}')
    else:
        if source_dir and os.path.isdir(source_dir):
            main(source_dir)
        else:
            print(f'Exception: source_dir: {source_dir}')
            print(f'Exception: target_dir isdir: {os.path.isdir(source_dir)}')


def main(source_dir):
    print(f'source_dir: {source_dir}')
    source_type_dir_list = search_source_path(source_dir)
    if source_type_dir_list:
        search_type_path(source_type_dir_list)


def search_source_path(source_dir):
    source_type_dir_list = []
    for root, dirs, _ in os.walk(source_dir):
        if not len(dirs):
            continue
        print(f"root:{root}\ndirs:{dirs}\n")
        for type_name in dirs:
            source_type_dir_list.append(os.path.join(root, type_name))
        print(f'source_type_path: {source_type_dir_list}')
    return source_type_dir_list


def get_barcode_from_path(file_path):
    file_name = os.path.split(file_path)[-1]
    print(f'file_name: {file_name}')
    barcode = ".".join(file_name.split('.')[:-3])
    return barcode


def search_type_path(dir_list):
    for dir_path in dir_list:
        file_names = glob.glob(os.path.join(dir_path, r'*.png'))
        barcode_dict = {}
        # print(f'{dir_path} file_names: {file_names}')
        for file_path in file_names:
            barcode = get_barcode_from_path(file_path)
            print(f'barcode: {barcode}')
            if barcode not in barcode_dict.keys():
                barcode_dict.update({barcode: []})
            barcode_dict[barcode].append(file_path)
        for barcode, file_list in barcode_dict.items():
            print(f'barcode_dict[{barcode}]: {file_list}')
            for i, current_file_path in enumerate(file_list):
                idx = '%02d' % (i+1)
                print(f'{current_file_path}: {idx}')
                split_list = current_file_path.split('.')
                print(f'split_list: {split_list}')
                split_list.insert(len(split_list)-1, idx)
                print(f'new split_list: {split_list}')
                new_file_path = '.'.join(split_list)
                print(f'new_file_path: {new_file_path}')
                os.renames(current_file_path, new_file_path)


if __name__ == '__main__':
    parse_argument()
