#!/bin/bash
# log_analyzer.sh
# Log File Analyzer: Extracts and summarizes error/warning lines from a log file.
# Usage: ./log_analyzer.sh <logfile>

# Extracts error and warning lines
grep_errors_warnings() {
    local logfile="$1"
    grep -Ei 'error|warning' "$logfile"
}

# Counts occurrences of errors and warnings
count_occurrences() {
    local logfile="$1"
    grep -Ei 'error|warning' "$logfile" | awk '{print $1}' | sort | uniq -c
}

# Prints a summary report
print_report() {
    local logfile="$1"
    echo "Summary of errors and warnings in $logfile:"
    count_occurrences "$logfile"
}

# Main script logic
main() {
    if [ $# -ne 1 ]; then
        echo "Usage: $0 <logfile>"
        exit 1
    fi
    if [ ! -f "$1" ]; then
        echo "Log file $1 not found."
        exit 2
    fi
    grep_errors_warnings "$1"
    print_report "$1"
}

main "$@"
