import re
import sys

# Read the .ora file and store it as a string
with open('../ora-parser/tnsnames.ora', 'r') as ora_file:
    ora_contents = ora_file.read()

# Define the database entry you want to extract
db_entry_name = sys.argv[1:]
print(db_entry_name)
# Use regular expressions to extract the HOST value
# host_pattern = rf'{db_entry_name}\s*=\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\)\(host\s*=\s*([^)]+)\)'
host_pattern = rf'{db_entry_name}\s*=\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\)\(host\s*=\s*([^)]+)\)\((?:(?!\)).)*\s*\)\)\s*\)\s*\((?:(?!\)).)*\s*\(Service_name\s*=\s*([^)]+)\)'
host_matches = re.search(host_pattern, ora_contents, re.DOTALL)

if host_matches:
    host = host_matches.group(1)
    service_name = host_matches.group(2)

    print(f"Host for {db_entry_name}: {host}")
    print(f"Service name for {db_entry_name}: {service_name}")
else:
    print(f"Database entry {db_entry_name} not found.")

# service_name_pattern = rf'{db_entry_name}\s*=\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\)\(host\s*=\s*([^)]+)\)\((?:(?!\)).)*\s*\)\)\s*\)\s*\((?:(?!\)).)*\s*\(Service_name\s*=\s*([^)]+)\)'
# service_name_matches = re.search(service_name_pattern, ora_contents, re.DOTALL)
# print(service_name_matches.group(2))

# if service_name_matches:
#     service_name_matches = service_name_matches.group(2)
#     print(f"Service name for {db_entry_name}: {service_name_matches}")
# else:
#     print(f"Database entry {db_entry_name} not found.")
