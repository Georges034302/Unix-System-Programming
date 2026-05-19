#!/bin/bash
# menu_tool.sh
# Menu-Driven Tool: Presents a menu and calls functions for each option.
# Usage: ./menu_tool.sh

# Shows the current date and time
show_date() {
    echo "Current date and time: $(date)"
}

# Lists files in the current directory
list_files() {
    echo "Files in $(pwd):"
    ls -lh
}

# Searches for a pattern in a file
search_text() {
    read -p "Enter filename: " filename
    if [ ! -f "$filename" ]; then
        echo "File not found."
        return
    fi
    read -p "Enter search pattern: " pattern
    grep --color=auto -n "$pattern" "$filename"
}

# Main menu loop
main_menu() {
    while true; do
        echo "\nMenu:"
        echo "1) Show date/time"
        echo "2) List files"
        echo "3) Search text in file"
        echo "4) Exit"
        read -p "Choose an option: " choice
        case $choice in
            1) show_date ;;
            2) list_files ;;
            3) search_text ;;
            4) echo "Goodbye!"; break ;;
            *) echo "Invalid option." ;;
        esac
    done
}

main_menu
