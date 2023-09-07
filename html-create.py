# Define data for the loop
data = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Create an HTML file
file_name = "output.html"

with open(file_name, "w") as file:
    # Write the HTML header
    file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>My HTML Page</title>\n</head>\n<body>\n")

    # Write data from the loop
    file.write("<ul>\n")
    for item in data:
        file.write(f"    <li>{item}</li>\n")
    file.write("</ul>\n")

    # Write the HTML footer
    file.write("</body>\n</html>")

print(f"HTML file '{file_name}' has been created.")
