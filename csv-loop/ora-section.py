import re

def extract_section(file_path, section_name):
    section_found = False
    section_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line contains the desired section
            if re.match(rf"{section_name}\s*=", line.strip()):
                section_found = True

            elif section_found and re.match(r'\w+\s*=', line.strip()):
                # Stop when reaching another section
                break
            elif section_found:
                # Collect lines within the section
                section_lines.append(line.strip())
    return section_lines

def extract_value(KeyName, line):
    pattern = rf"\({KeyName}\s*=\s*([^)]+)\)"        
    match = re.search(pattern, line, re.IGNORECASE)
    # value = ""
    
    if  re.search(pattern, line, re.IGNORECASE):
        value = match.group(1)
    return value    
            
         

# Example usage
file_path = 'tnsnames.ora'  # Replace with the actual path to your file
section_name = 'ORCL12'

section_content = extract_section(file_path, section_name)


if section_content:
    # print(f"Contents of {section_name}:")
    for line in section_content:
        try: 
            HOST = extract_value("HOST", line)
        except:
            Found = "false"
        try: 
            SERVICE_NAME = extract_value("SERVICE_NAME", line)
        except:
            Found = "false"

    
    print(f"Host is {HOST}")
    print(f"SERVICE_NAME is {SERVICE_NAME}")
else:
    print(f"Section {section_name} not found in the file.")
