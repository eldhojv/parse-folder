# Parse-Folder
  Script to traverse a given directory to display and extract all gzipped files under the directory at any level.

### Functions 

  1. display all gzipped files under the directory at any level (able to display gzipped files regardless of having .gz suffix in the filename)
  2. gunzip the files inplace:
        - gzipped files with .gz suffix in filename is gunzipped to without .gz suffix in the end, overwriting any existing files
        - gzipped files without .gz suffix in the filename is gunzipped to same path, replacing the original file
