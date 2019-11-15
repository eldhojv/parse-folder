# Parse-Folder
  Script to traverse a given directory to display and extract all gzipped files under the directory at any level.

### Functions 

  1. display all gzipped files under the directory at any level (able to display gzipped files regardless of having .gz suffix in the filename)
  2. gunzip the files inplace:
        - gzipped files with .gz suffix in filename is gunzipped to without .gz suffix in the end, overwriting any existing files
        - gzipped files without .gz suffix in the filename is gunzipped to same path, replacing the original file


## Usage

````
usage: run.py [-h] [--source_dir source-directory/Images] --dryrun true/false

Recursively parse folder to display all gzipped files under the directory at
any level and to gunzip the files inplace

optional arguments:
  -h, --help            show this help message and exit
  --source_dir source-directory/Data-directory
                        Source directory to parse
  --dryrun true/false   True - to display all gzipped files /#/ False - to gunzip all files in place
````

## Example
  
  Display all gzipped files (gzip files with and without .gz extensions)
  ````
  python run.py --source_dir "E:\parse-folder\Data-directory" --dryrun true
  ````  
  Or you can run simply with defualt config
  (data directory should be present in the root directory with folder name Data-directory)
  ````
  python run.py --dryrun true
  ````
  Extract all gzipped files
  ````
  python run.py --source_dir "E:\parse-folder\Data-directory" --dryrun true
  ````
  ----
  To recursively parse and convert files to gzip in a particular directory
  ````
  python convert_to_gzip.py
  ````
