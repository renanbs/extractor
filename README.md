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

## How to run
It will search recursively for all .rar files and extract it.
