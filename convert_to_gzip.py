import os
import shutil
import gzip

ROOT_DIR = ''
DIRECTORY = 'Data-directory'  # change to your folder name 
DEFAULT_DATA_DIRECTORY = os.path.join(ROOT_DIR, DIRECTORY)

for root, dirs, files in os.walk(DEFAULT_DATA_DIRECTORY):
    for each_file in files:
        with open(os.path.join(root, each_file), 'rb') as f_in:
            with gzip.open(os.path.join(root, each_file)+'.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)