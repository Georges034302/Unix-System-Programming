#!/bin/bash
# resource_monitor.sh
# System Resource Monitor: Displays CPU, memory, and disk usage, and alerts if thresholds are exceeded.
# Usage: ./resource_monitor.sh

# Displays CPU usage
show_cpu_usage() {
    echo "CPU Usage:" 
    top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4 "% used"}'
}

# Displays memory usage
show_memory_usage() {
    echo "Memory Usage:"
    free -h | awk '/^Mem:/ {print $3 "/" $2 " used (" $3*100/$2 "% )"}'
}

# Displays disk usage
show_disk_usage() {
    echo "Disk Usage:"
    df -h / | awk 'NR==2 {print $3 "/" $2 " used (" $5 ")"}'
}

# Checks if usage exceeds threshold and alerts
check_thresholds() {
    local cpu_threshold=80
    local mem_threshold=80
    local disk_threshold=80
    local cpu=$(top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    local mem=$(free | awk '/^Mem:/ {print int($3*100/$2)}')
    local disk=$(df / | awk 'NR==2 {gsub("%", "", $5); print $5}')
    if [ "${cpu%.*}" -gt $cpu_threshold ]; then
        echo "[ALERT] CPU usage above $cpu_threshold%: $cpu%"
    fi
    if [ "$mem" -gt $mem_threshold ]; then
        echo "[ALERT] Memory usage above $mem_threshold%: $mem%"
    fi
    if [ "$disk" -gt $disk_threshold ]; then
        echo "[ALERT] Disk usage above $disk_threshold%: $disk%"
    fi
}

# Main script logic
main() {
    show_cpu_usage
    show_memory_usage
    show_disk_usage
    check_thresholds
}

main
