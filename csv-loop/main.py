import configparser
import sys
import csv
import subprocess
import re

# Define the input and output file paths
input_file = 'data.csv'
output_file = 'output_data.csv'  # Use a different filename for the output

ini_file = "./data.ini"
ora_file = "./tnsnames.ora"


# Open the CSV file for reading
with open(input_file, 'r', newline='') as infile:
    with open(output_file, 'w', newline='') as outfile:
       # Create a CSV reader
       csvreader = csv.reader(infile)
       csvwriter = csv.writer(outfile)
       column_names = ["SUBJECT_AREA", "CONNECTION_NAME", "CONNECTION_STRING", "CNX_SUBTYPE_NAME", "HOST_NAME", "DB_NAME" ]  

       csvwriter.writerow(column_names)
       
       # Skip the header row if it contains column names
       next(csvreader)
       
       # Iterate through the rows in the CSV file
       for row in csvreader:
           SUBJECT_AREA, CONNECTION_NAME, CONNECTION_STRING, CNX_SUBTYPE_NAME = row  # Assuming three columns in the CSV
           if CNX_SUBTYPE_NAME == "Oracle":
              # Define the command to run, including the script name and arguments
              with open(ora_file, 'r') as ora_file:
                  ora_contents = ora_file.read()
              
              # Define the database entry you want to extract
              db_entry_name = CONNECTION_STRING
              # try:
              host_pattern = rf'{db_entry_name}\s*=\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\)\s*\(HOST\s*=\s*([^)]+)\)\s*\((?:(?!\)).)*\)\s*\)\s*\)\s*\((?:(?!\)).)*\s*\(SERVICE_NAME\s*=\s*([^)]+)\)'
              host_matches = re.search(host_pattern, ora_contents, re.DOTALL)
              if host_matches == None:
                host_pattern = rf'{db_entry_name}\s*=\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\((?:(?!\)).)*\s*\)\s*\(HOST\s*=\s*([^)]+)\)\s*\((?:(?!\)).)*\)\s*\)\s*\((?:(?!\)).)*\s*\(SERVICE_NAME\s*=\s*([^)]+)\)'
                host_matches = re.search(host_pattern, ora_contents, re.DOTALL)
              
              if host_matches:
                  host = host_matches.group(1)
                  service_name = host_matches.group(2)
              
                  row.append(host)
                  row.append(service_name)
                  csvwriter.writerow(row)
              else:
                  row.append("N/A")
                  row.append("N/A")
                  csvwriter.writerow(row)
                  print(f"ORA Database entry {db_entry_name} not found.")
                             
   
           if CNX_SUBTYPE_NAME == "ODBC":             
              # Create a ConfigParser object and read the INI file
              config = configparser.ConfigParser()
              config.read(ini_file)
              try: 
                 address = config.get(CONNECTION_STRING, 'Address')
                 address = address.split("\\")
                 address = address[0]
                 db_name = config.get(CONNECTION_STRING, 'Database')
                 row.append(address)
                 row.append(db_name)
                 csvwriter.writerow(row)

              except: 
                 hostname = config.get(CONNECTION_STRING, 'HostName')
                 hostname = hostname.split("\\")
                 hostname = data[0]
                 db_name = config.get(CONNECTION_STRING, 'Database')
                 row.append(hostname)
                 row.append(db_name)
                 csvwriter.writerow(row) 

print(f"{output_file} file is generated.. :)")  



