from pathlib import Path
import subprocess

path_list = Path(".").glob('**/*.rar')
for path in path_list:
    path_in_str = str(path)
    print("Extracting: " + path_in_str)
    out = subprocess.run(["unrar", "e", path_in_str], stdout=subprocess.DEVNULL)
    if not out.returncode:
        print("[  OK ] " + path_in_str)
    else:
        print("[ERROR] " + path_in_str)
