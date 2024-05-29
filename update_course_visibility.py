import requests
import os
from config import access_token, base_url
headers = {"Authorization": "Bearer " + access_token}

# Define a list of course IDs to update
course_ids = []


# Define the payload to update the course visibility to "Institution"
payload = {"course": {"is_public": False, "is_public_to_auth_users": True, "hide_final_grades": False}}

# Loop through each course ID and update the course visibility
for course_id in course_ids:
    url = f"{base_url}/courses/{course_id}"
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"Visibility of course {course_id} updated")
    else:
        print(f"Failed to update visibility of course {course_id}. Response: {response.json()}")
