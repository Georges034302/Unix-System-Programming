#!/bin/bash
# batch_rename.sh
# Batch File Renamer: Adds a prefix to all files in a directory.
# Usage: ./batch_rename.sh <directory> <prefix>

# Renames files by adding a prefix
rename_files() {
    local dir="$1"
    local prefix="$2"
    for file in "$dir"/*; do
        if [ -f "$file" ]; then
            local base=$(basename "$file")
            mv "$file" "$dir/$prefix$base"
            echo "Renamed $base to $prefix$base"
        fi
    done
}

# Validates directory existence
validate_directory() {
    if [ ! -d "$1" ]; then
        echo "Directory $1 does not exist."
        exit 1
    fi
}

# Main script logic
main() {
    if [ $# -ne 2 ]; then
        echo "Usage: $0 <directory> <prefix>"
        exit 1
    fi
    validate_directory "$1"
    rename_files "$1" "$2"
}

main "$@"
