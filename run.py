from modules.cmdparser import *
from modules.parsefolder import *

if __name__ == "__main__":
    args = parse_arguments()

    if args:
        parse_folder(args)
        # print("ok")
    else:
        exit(1)



