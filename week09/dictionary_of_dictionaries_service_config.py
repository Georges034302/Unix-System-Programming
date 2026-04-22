#!/usr/bin/env python3
"""
Store service configuration in a dictionary of dictionaries.
Demonstrates: nested dictionaries, nested access, update, reporting.
"""

services = {
    "nginx": {"status": "running", "port": 80},
    "ssh": {"status": "running", "port": 22},
    "db": {"status": "stopped", "port": 5432},
}

services["db"]["status"] = "running"

print("Service configuration:")
for service_name in services:
    config = services[service_name]
    print(
        f"  {service_name:8} -> status: {config['status']:8} port: {config['port']}"
    )
