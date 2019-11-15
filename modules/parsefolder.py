import os
import gzip
import shutil
from modules.utils import *


ROOT_DIR = ''
DEFAULT_SOURCE_DIR = os.path.join(ROOT_DIR, 'Data-directory')

def parse_folder(args):
    file_list = []
    if not args.source_dir:
        directory = DEFAULT_SOURCE_DIR
    else:
        directory = args.source_dir


    for root_dir, dirs, files in os.walk(directory, topdown=False):
            for each_file in files:
                if is_gzipped(root_dir, each_file):
                    file_list.append(os.path.join(root_dir, each_file))


    if args.dryrun.lower() == 'true':
        print("---------------------------------------------------------------------")
        print("**** gzipped files under the directory at any levels **** ")
        for each_file in file_list:
            print(each_file)
        print("---------------------------------------------------------------------")

    else:
        for each_file in file_list:
            if not each_file.endswith('.gz'):
                dest_file_name = each_file  #destination file name will be same as each_file since it doesn't have .gz extension
                file_name, file_ext = os.path.splitext(each_file)
                dummy_file = os.path.split(each_file)[0]+'\\dummy'+file_ext
            else:
                gz_file_name, gz_file_ext = os.path.splitext(each_file) 
                dest_file_name = gz_file_name # destination file name will be split of gz_file_name eg: split of "filename.txt.gz" = "filename.txt"
                file_name, file_ext = os.path.splitext(gz_file_name)
                dummy_file = os.path.split(each_file)[0]+'\\dummy'+file_ext

            with gzip.open(each_file, 'rb') as f_rd:
                with open(dummy_file, 'wb') as f_wt:
                    shutil.copyfileobj(f_rd, f_wt)
                    f_rd.close()
                    f_wt.close()

            os.remove(each_file)
            if os.path.exists(dest_file_name):
                os.remove(dest_file_name)
            os.rename(dummy_file, dest_file_name)


                

    