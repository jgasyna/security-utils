# Security Utils

This project contains source code and supporting files for a variery of system level security tools and utilities

#### FILE UTILS

- recursive_file_dups.py - Run this script to find identical files that may be named differently
```bash
python recursive_file_dups.py <path>
```
Notes:
 - Assumes python 3
 - The big trip up here was getting the absolute path - Watch out for the pesky Hidden .DS_Store if using a mac (Removed from Finder in Mojave.  Yea thanks for that Apple!)
 - If no path is given, it runs in current path
 
 