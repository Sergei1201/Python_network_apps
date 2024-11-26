# Removing files
import os
import shutil

path = 'test'
try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("File has not been found")
except PermissionError:
    print("Permission error")
except OSError:
    print("You cannot delete a folder which is not empty")
else:
    print(f"{path} has been deleted successfully")
