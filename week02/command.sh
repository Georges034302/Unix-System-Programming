#!/bin/bash
# command.sh — Linear Unix file operations demo (no functions, no menu)
# Demonstrates core file operations step by step.

touch f{1..3}
mv f[0-9] dir

# 1. Create a new file
touch demo_file.txt
echo "Created demo_file.txt"

# 2. List files in the current directory
echo "Listing files:"
ls -lh

# 3. Change file permissions
chmod 600 demo_file.txt
echo "Changed permissions of demo_file.txt to 600 (rw-------)"

# 4. Copy the file
cp demo_file.txt copy_of_demo.txt
echo "Copied demo_file.txt to copy_of_demo.txt"

# 5. Move/rename the copy
mv copy_of_demo.txt moved_demo.txt
echo "Renamed copy_of_demo.txt to moved_demo.txt"

# 6. Show file details
echo "File details:"
ls -l demo_file.txt moved_demo.txt

# 7. Remove files
rm -f demo_file.txt moved_demo.txt
echo "Removed demo_file.txt and moved_demo.txt"

