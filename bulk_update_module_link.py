import requests
import os
import canvasapi
from config import access_token, base_url
headers = {"Authorization": "Bearer " + access_token}

# Define a list of course IDs to update
course_ids = [22217, 22198, 22205, 23784, 22213, 22215, 22190, 22202, 22194, 22200, 22193, 22199, 22197, 22204, 22191, 22208, 22216, 22206, 22192, 22207, 22210, 22201, 22214, 22195, 22196, 22203, 22209, 22211, 23200, 22212]
#course_ids = [23424]

# Define a dict of modules with title as key and module id as value
update_link_dict = {
    # "Year 5 Diversity Adjustments": "https://docs.google.com/spreadsheets/d/1EfQ17a8W8BCP0BWaYVtMZ_JnUyZ0bRzAjGOSOqfDMZY/edit",
    # "Year 6 Diversity Adjustments": "https://docs.google.com/spreadsheets/d/1OFYmiWGf9q3QXurfOuKdPvF-pe1WqZlgh_zBlyZ40X0/edit",
    # "Year 7 Diversity Adjustments": "https://docs.google.com/spreadsheets/d/1DwGqe3lr6nfhhV72eR0zjKtHQ4FAkpY7w67_odQZPCA/edit",
    # "Year 8 Diversity Adjustments": "https://docs.google.com/spreadsheets/d/1tfT4H1_G8T4puaX5iYNvk330yiC5tleavferMAIKHug/edit",
    # "Year 9 Diversity Adjustments": "https://docs.google.com/spreadsheets/d/1X9JKb39cijp6nFIChLxskZQeIw_IF_DQaJi8TBFSLFA/edit",
    # "Year 10 Diversity Adjustments": "https://docs.google.com/spreadsheets/d/1uMoEQdxb6z_b9wp7BgKOOpQBeW6lQKCeXM-iksbGtIs/edit",
    # "2023 - Year 11 - Program Adjustments": "https://docs.google.com/spreadsheets/d/1nbVtb4OU5627l8JRkcp3XqG4Ae9Ob8xvqDMegrnr4nw/edit",
    "Year 12 Diversity Adjustments": "https://docs.google.com/spreadsheets/d/1zo4FR51qN9u7RiAc6M3vNZEjlO8gDu9AcwZBgL4ux4A/edit",

}

update_name_dict = {
    "2023 - Year 11 - Program Adjustments": "Year 11 - Diversity Adjustments",
}

canvas = canvasapi.Canvas(base_url, access_token);

for cid in course_ids:
    course = canvas.get_course(cid)
    modules = course.get_modules()

    for module in modules:
        #get module items
        items = module.get_module_items()

        for module_item in items:
            # find the module by name
            if module_item.title in update_link_dict:
                #module_item.edit(external_url=update_link_dict[module_item.title], module_item=module_item)
                requests.put(base_url + "/api/v1/courses/" + str(cid) + "/modules/" + str(module.id) + "/items/" + str(module_item.id), headers=headers, data={"module_item[external_url]": update_link_dict[module_item.title]})
                print("Updated module link: " + module_item.title + " in course: " + course.name)

            if module_item.title in update_name_dict:
                #module_item.edit(title=update_name_dict[module_item.title], module_item=module_item)
                requests.put(base_url + "/api/v1/courses/" + str(cid) + "/modules/" + str(module.id) + "/items/" + str(module_item.id), headers=headers, data={"module_item[title]": update_name_dict[module_item.title]})
                print("Updated module name: " + module_item.title + " in course: " + course.name)



