from canvasapi import Canvas
from bs4 import BeautifulSoup
import requests
import os
from config import access_token, base_url, account_id

# set the CANVAS_SESSION cookie to your Canvas session cookie
CANVAS_SESSION=os.environ['CANVAS_SESSION']

student_user_id = 111111
parent_user_id = 222222

canvas = Canvas(base_url, access_token)


# get a user by SIS ID
user = canvas.get_user(student_user_id)


# since we don't have access to get the student's enrollments from the api, we need to scrape the user's profile page for the enrollments.
# this is a bit of a hack, but it works.
profile_page = requests.get(f"{base_url}/accounts/{account_id}/users/{user.id}", cookies={'canvas_session': CANVAS_SESSION})
soup = BeautifulSoup(profile_page.text, 'html.parser')

# get the div called "courses" which contains the list of courses the user is enrolled in
courses_div = soup.find('div', id='courses_list')

# get the ul element which contains the list of courses
courses_ul = courses_div.find('ul')

# find the li elements with class "active clearfix"

user_active_courses_li = courses_ul.find_all('li', class_='active clearfix')

# loop through the courses and print the course name and id

user_active_courses = []
for li_course in user_active_courses_li:
    # find the the link element and get the href attribute
    course_link = li_course.find('a')
    course_id = course_link['href'].split('/')[2]
    user_active_courses.append(canvas.get_course(course_id))

parent = canvas.get_user(parent_user_id)

print("Please confirm the following details are correct:")
print(f"Student: {user.name} ({user.id})")
print(f"Parent: {parent.name} ({parent.id})")
print(f"Courses: {', '.join([course.name for course in user_active_courses])}")

confirm = input("Continue? (y/n): ")

if confirm != 'y':
    print("Aborting...")
    exit(1)

for course in user_active_courses:
    # enroll the parent as an observer to the student in the course
    print(f"Enrolling {parent.name} ({parent.id}) as an observer to {user.name} ({user.id}) in {course.name} ({course.id})")
    course.enroll_user(parent, 'ObserverEnrollment', enrollment={'associated_user_id': user.id})


print("done!")