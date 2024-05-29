import requests
import canvasapi
from config import access_token, base_url
import csv

canvas = canvasapi.Canvas(base_url, access_token)

# read the module_assignment_ids.csv file
with open('module_assignment_ids.csv', mode='r') as file:
    csvFile = csv.reader(file)
    module_assignment_ids = list(csvFile)
    for ids in module_assignment_ids:
        course = canvas.get_course(ids[0])
        assignment = course.get_assignment(ids[2])
        assignment.delete()

        module = course.get_module(ids[1])
        module.delete()

        print(f"Deleted module {ids[1]} and assignment {ids[2]} in course {ids[0]}")


print("Done deleting modules and assignments")

