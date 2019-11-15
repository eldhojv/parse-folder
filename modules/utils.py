import os

def is_gzipped(root_dir, file):
    with open(os.path.join(root_dir,file), "rb") as rf:
        sig = rf.read(3)
    return sig == b'\x1f\x8b\x08'