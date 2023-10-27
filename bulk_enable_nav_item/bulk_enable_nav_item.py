import os
import canvasapi
from config import access_token, base_url, account_id

canvas = canvasapi.Canvas(base_url, access_token);
account = canvas.get_account(account_id)
courses = account.get_courses()
tab_id = "context_external_tool_1111"
for course in courses:
    tabs = course.get_tabs()
    for tab in tabs:
        if tab.id == tab_id:
            tab.update(hidden=False)
            print("Enabled nav item on course " + str(course.name))