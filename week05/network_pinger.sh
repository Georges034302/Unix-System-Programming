#!/bin/bash
# network_pinger.sh
# Network Pinger: Pings a list of hosts and reports reachability.
# Usage: ./network_pinger.sh <host1> <host2> ...

# Pings a single host and reports status
ping_host() {
    local host="$1"
    # Use -w 1 for compatibility with IPv4/IPv6
    if ping -c 1 -w 1 "$host" &> /dev/null; then
        echo "$host is reachable."
    else
        echo "$host is unreachable."
    fi
}

# Pings all hosts provided as arguments
ping_all_hosts() {
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <host1> <host2> ..."
        exit 1
    fi
    for host in "$@"; do
        ping_host "$host"
    done
}

ping_all_hosts "$@"
