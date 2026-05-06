#!/usr/bin/env python3
"""
Store service configuration in a dictionary of dictionaries.
Demonstrates: nested dictionaries, nested access, update, reporting.
"""

# Each service maps to a nested dictionary with status and port fields.
services = {
    "nginx": {"status": "running", "port": 80},
    "ssh": {"status": "running", "port": 22},
    "db": {"status": "stopped", "port": 5432},
}

# Update nested value for an existing service.
services["db"]["status"] = "running"
# Add a new service with a non-standard status (not running or stopped).
services["rdp"] = {"status": "maintenance", "port": 3389}

# Print each service name alongside its status and port.
print("Service configuration:")
for service_name in services:
    config = services[service_name]  # Access inner dictionary for this service.
    print(
        f"  {service_name:8} -> status: {config['status']:8} port: {config['port']}"
    )
