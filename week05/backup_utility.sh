#!/bin/bash
# backup_utility.sh
# Backup Utility: Backs up files/directories to a backup/ folder with a timestamp.
# Usage: ./backup_utility.sh <source_path>

# Creates a backup directory if it doesn't exist
create_backup_dir() {
    [ -d backup ] || mkdir backup
}

# Performs the backup
backup_item() {
    local src="$1"
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local dest="backup/$(basename "$src")_$timestamp"
    if [ -d "$src" ]; then
        cp -r "$src" "$dest"
    else
        cp "$src" "$dest"
    fi
    echo "$dest"
}

# Verifies backup success
verify_backup() {
    local dest="$1"
    if [ -e "$dest" ]; then
        echo "Backup successful: $dest"
    else
        echo "Backup failed."
    fi
}

# Logs the backup operation
log_backup() {
    local src="$1"
    local dest="$2"
    echo "[$(date)] Backed up $src to $dest" >> backup/backup.log
}

# Main script logic
main() {
    if [ $# -ne 1 ]; then
        echo "Usage: $0 <source_path>"
        exit 1
    fi
    if [ ! -e "$1" ]; then
        echo "Source $1 does not exist."
        exit 2
    fi
    create_backup_dir
    local dest
    dest=$(backup_item "$1")
    verify_backup "$dest"
    log_backup "$1" "$dest"
}

main "$@"
