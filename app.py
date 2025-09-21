import requests
import os

# API Configuration
try:
    api_key = “sk-6Ng7YDAkl0D5z20vAh7tPkmWn5hCTcZGIcl_wRiQ5NQ”
except KeyError:
    raise ValueError("LANGFLOW_API_KEY environment variable not found. Please set your API key in the environment variables.")

url = "http://localhost:7860/api/v1/run/30d9ce86-194f-44ba-a15a-f822c3ac4f57"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "hello world!"
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key  # Authentication key from environment variable
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
