import os

filepath = "82_builtin_modules.py"
if os.path.exists(filepath):
    print("The file exists")
else:
    print("The file does not exist")