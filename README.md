# extractor
Simple python script to extract multiple rar files

The objective of this script is to simple extract rar files that are in a structure like this

```bash
$ ls -laR

drwxr-xr-x 2 renan users 4.0K Aug 24 09:08 The.File
drwxr-xr-x 2 renan users 4.0K Aug 23 23:33 The.File.2

./The.File:
-rw-r--r-- 1 renan users 50000000 Aug 23 23:26 the.file.r00
-rw-r--r-- 1 renan users 50000000 Aug 23 23:29 the.file.r01
-rw-r--r-- 1 renan users 50000000 Aug 23 23:29 the.file.r02
-rw-r--r-- 1 renan users 50000000 Aug 23 23:26 the.file.r03
-rw-r--r-- 1 renan users 50000000 Aug 23 23:26 the.file.rar

./The.File.2:
-rw-r--r-- 1 renan users 50000000 Aug 23 23:32 the.file.2.r00
-rw-r--r-- 1 renan users 50000000 Aug 23 23:32 the.file.2.r01
-rw-r--r-- 1 renan users 50000000 Aug 23 23:31 the.file.2.r02
-rw-r--r-- 1 renan users 50000000 Aug 23 23:34 the.file.2.r03
-rw-r--r-- 1 renan users 50000000 Aug 23 23:30 the.file.2.rar
```

## Install
Just copy the script "extractor.py" to the directory that has this structure. 


## Dependencies
The only dependencies is to have unrar installed. I haven't done any checks for it.


## How to run
It will search recursively for all .rar files and extract it.
```bash
$ python extractor.py
Extracting: The.File/the.file.rar
[  OK ] The.File/the.file.rar
Extracting: The.File.2/the.file.2.rar
[  OK ] The.File.2/the.file.2.rar
```

This is the final result
```bash
drwxr-xr-x 2 renan users 4.0K Aug 24 09:08 The.File
-rw-r--r-- 1 renan users 1.1G Aug 18 16:16 The.File.mkv
drwxr-xr-x 2 renan users 4.0K Aug 23 23:33 The.File.2
-rw-r--r-- 1 renan users 989M Aug 18 16:20 The.File.2.mkv
```
