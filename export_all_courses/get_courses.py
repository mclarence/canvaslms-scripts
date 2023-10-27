from canvasapi import Canvas
import os 
from config import access_token, base_url, account_id

canvas = Canvas(base_url, access_token)
enrollment_state = 'active'
courses = canvas.get_account(account_id).get_courses(enrollment_state)

# write to csv file called courses.csv   
with open('courses.csv', 'w') as f:
    f.write('id,name\n')
    for course in courses:
        f.write(f'{course.id},{course.name}, {course.course_code}, {course.enrollment_term_id}\n')
    
print("Done!")

