import json
import requests


publickey = 'sfd'
apikey = 'sfdsfds'

groupId = 'groupId'
appId = 'appId'


## authentication

url = "https://services.cloud.mongodb.com/api/admin/v3.0/auth/providers/mongodb-cloud/login"

payload = {
    "username": publickey,
    "apiKey": apikey
}


payload_json = json.dumps(payload)     

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.post(url, headers=headers, json=payload_json)

# Parse the JSON response
response_data = response.json()

# Extract the access_token
access_token = response_data.get("access_token")

# Get all triggers
url_template = "https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/triggers"

url = url_template.format(groupId=groupId, appId=appId)
payload = ""

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'   # Replace with your actual authorization token
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

# Loop through each item in the data list
for item in data:

    # Check if 'disabled' is False
    if not item.get('disabled', True):  # Default to True if 'disabled' key is missing
        _id = item['_id']
        config = item['config']
        event_processors = item['event_processors']

        # Construct the payload with the extracted config and event_processors
        payload = {
            "name": item['name'],
            "type": item['type'],
            "function_id": item['function_id'],  # Use the function_id from the data
            "config": config,
            "event_processors": event_processors
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'   # Replace with your actual authorization token
        }

        # Convert the payload to JSON format
        payload_json = json.dumps(payload)

        # Enable a trigger
        url_template = "https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/triggers/{triggerId}"


        url = url_template.format(groupId=groupId, appId=appId, triggerId=_id)

        # Send the PUT request
        response = requests.request("PUT", url, headers=headers, data=payload_json)

        # Print the response
        print(f"Response for _id {_id}:")
        print(response.text)
        print('-' * 50)
    else:
        print(f"Skipping _id {item['_id']} because it is disabled.")

    if not item.get('disabled', True):  # Default to True if 'disabled' key is missing ##TODO check the suspended status
        _id = item['_id']

        # Resume a trigger
        url_template = "https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/triggers/{triggerId}/resume"


        url = url_template.format(groupId=groupId, appId=appId, triggerId=_id)

        payload = ""

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'   # Replace with your actual authorization token
        }
        
        # Send the PUT request
        response = requests.request("PUT", url, headers=headers, data=payload)

        # Print the response
        print(f"Response for _id {_id}:")
        print(response.text)
        print('-' * 50)
    else:
        print(f"Skipping _id {item['_id']} because it is already running.")
