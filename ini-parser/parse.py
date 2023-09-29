import configparser

# Create a ConfigParser object and read the INI file
config = configparser.ConfigParser()
config.read('data.ini')

# Access a value from the INI file
value = config.get('TEST1', 'Address')
print(value)

# Split the string into a list of parts using the delimiter
data = value.split("/")

hostname = data[0]
db_name = data[1]
print(hostname)
print(db_name)