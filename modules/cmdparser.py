import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively parse folder to display all gzipped files under the directory at any level and to gunzip the files inplace")
    parser.add_argument("--source_dir", required=False, metavar="source-directory/Images",
                        help="Source directory to parse")
    parser.add_argument("--dryrun", required=True, metavar="true/false", choices=['true','false'],
                        help="True - to display all gzipped files /#/ False - to gunzip all files in place")
    return parser.parse_args()


parse_arguments()