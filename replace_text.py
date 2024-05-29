from canvasapi import Canvas
import os 
from config import access_token, base_url, account_id
import requests
import re
canvas = Canvas(base_url, access_token)
course_ids = [22194, 22208, 22193, 22195, 22206, 22213, 22205, 22204, 22191, 22199, 22197, 22211, 22201, 22212, 22192, 22215, 22210, 22190, 22196, 22214, 23784, 22198, 22216, 22209, 22203, 22207, 22202, 22217, 23200, 22200, 23452, 23443, 23395, 23438, 23412, 23431, 23396, 23436, 23393, 23441, 23432, 23419, 23423, 23415, 23403, 23404, 23401, 23455, 23437, 23420, 23414, 23434, 23448, 23433, 23422, 23446, 23397, 23453, 23450, 23394, 23426, 23399, 23442, 23409, 23405, 23411, 23427, 23445, 23398, 23402, 23400, 23407, 23425, 23421, 23429, 23410, 23444, 23413, 23406, 23458, 23454, 23416, 23418, 23447, 23449, 23408, 23435, 23451, 23417, 23457, 23424, 23440, 23439, 23428, 23430]

for id in course_ids:
    course = canvas.get_course(id)
    pages = course.get_pages()
    for page in pages:
        if page.title == 'Compliance Documentation':
            response = requests.get(f'{base_url}/api/v1/courses/{id}/pages/{page.url}', headers={'Authorization': f'Bearer {access_token}'}).json()
            content = response['body']
            #content = content.replace('Teacher Register', 'Teacher Evaluations and Registers')
            # case insensitive replace
            content = re.sub(r'(?i)teacher register', 'Teacher Evaluations and Registers', content)
            # update the page
            page.edit(wiki_page={'body': content})
            print(f'Updated page {page.title} in course {course.name}')
