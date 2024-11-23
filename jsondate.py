import datetime
import ast
import json

# Get current date
current_date_time = datetime.datetime.now()
current_date = current_date_time.strftime('%d/%m/%Y')

# Specify the path to the JSON file
file_path = "C:\\Users\\micha\\AppData\\Roaming\\Code\\User\\snippets\\c.json"

# Load and parse the JSON file using ast
with open(file_path, 'r') as json_file:
    json_text = json_file.read()
    json_data = ast.literal_eval(json_text)

# Update the "DATE" field in the "Start Design" snippet
if "Start Design" in json_data:
    for i, line in enumerate(json_data["Start Design"]["body"]):
        if "DATE:" in line:
            json_data["Start Design"]["body"][i] = f"DATE: {current_date}"
            break

# Write JSON data back to file
with open(file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print("JSON data has been updated with the current date:", current_date)
