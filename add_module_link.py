import requests
import os
from config import access_token, base_url
from canvasapi import Canvas

canvas = Canvas(base_url, access_token)

course_sis_ids = ["85161_8EN_2024", "85161_7PIP_2024", "85161_7SCI_2024", "85161_7PD_2024", "85161_7MA_2024", "85161_8SCI_2024", "85161_7EN_2024", "85161_7MEET_2024", "85161_7HSIE_2024", "85161_7RE_2024", "85161_8VA_2024", "85161_8PD_2024", "85161_8MEET_2024", "85161_8MA_2024", "85161_8MU_2024", "85161_8HSIE_2024", "85161_8JAP_2024", "85161_7VA_2024", "85161_7TAS_2024", "85161_8TAS_2024", "85161_8RE_2024"]

for course_sis_id in course_sis_ids:
    course = canvas.get_course(course_sis_id, use_sis_id=True)
    course_code = course_sis_id.split("_")[1]

    #get the modules
    modules = course.get_modules()

    for module in modules:
        if module.name == "Teacher Course Information - DO NOT PUBLISH":
            if course_code.startswith("7"):
                module.create_module_item({
                    "title": "Year 7 Diversity Adjustments",
                    "type": "ExternalUrl",
                    "external_url": "https://docs.google.com/spreadsheets/d/1DwGqe3lr6nfhhV72eR0zjKtHQ4FAkpY7w67_odQZPCA/edit?usp=drive_link",
                    "position": 4,
                    "new_tab": True
                
                })
                print("Added module item to " + course_sis_id)

            if course_code.startswith("8"):
                module.create_module_item({
                    "title": "Year 8 Diversity Adjustments",
                    "type": "ExternalUrl",
                    "external_url": "https://docs.google.com/spreadsheets/d/1tfT4H1_G8T4puaX5iYNvk330yiC5tleavferMAIKHug/edit?usp=drive_link",
                    "position": 4,
                    "new_tab": True
                })
                print("Added module item to " + course_sis_id)
