import requests
import os
from config import access_token, base_url
headers = {"Authorization": "Bearer " + access_token}

# Define a list of course IDs to update
course_ids = [
    23456,
    23394,
    23393,
    23395,
    23396,
    23397,
    23398,
    23399,
    23400,
    23401,
    23402,
    24674,
    23405,
    23406,
    23407,
    23408,
    23409,
    23410,
    23411,
    23412,
    23354,
    23355,
    23356,
    23357,
    23358,
    24677,
    23359,
    23360,
    23361,
    23362,
    23353,
    23364,
    23365,
    23366,
    23367,
    23369,
    24678,
    23370,
    23371,
    23372,
    23368,
    23363,
    23374,
    23375,
    23376,
    24679,
    23377,
    23378,
    23379,
    23380,
    23381,
    23382,
    23373,
    23384,
    23385,
    23386,
    23387,
    24680,
    23388,
    23389,
    23390,
    23391,
    23392,
    23383,
    23434,
    23429,
    23428,
    23451,
    23430,
    23413,
    23437,
    23414,
    23415,
    23416,
    23432,
    24681,
    23448,
    23438,
    23417,
    23431,
    23418,
    23419,
    23444,
    23436,
    23446,
]


# Define the payload to update the course visibility to "Institution"
payload = {"course": {"hide_final_grades": True}}

# Loop through each course ID and update the course visibility
for course_id in course_ids:
    url = f"{base_url}/api/v1/courses/{course_id}"
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"hide totals settings of course {course_id} updated")
    else:
        print(f"Failed to update hide totals settings of course {course_id}. Response: {response.json()}")
