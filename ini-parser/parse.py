import configparser
import sys

# Create a ConfigParser object and read the INI file
config = configparser.ConfigParser()
config.read('../ini-parser/data.ini')
CONNECTION_STRING = sys.argv[1:]

print(CONNECTION_STRING)

# Access a value from the INI file
value = config.get(CONNECTION_STRING[0], 'Address')

# Split the string into a list of parts using the delimiter
data = value.split("\\")

hostname = data[0]
db_name = data[1]
print(hostname)
print(db_name)