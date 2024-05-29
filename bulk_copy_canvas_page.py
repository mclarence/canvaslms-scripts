import requests
import os
from config import access_token, base_url

# Set the source course ID
source_course_id = ''

dest_page_title = 'my-page-title'
source_page_id = 'my-page-id'

copy_into_new_module = False
new_module_name = 'my-module-name'

# A list of destination course IDs to copy the page to
courses = []

for destination_course_id in courses:
    try:
        # Make a GET request to retrieve the source page details
        response = requests.get(f'{base_url}/courses/{source_course_id}/pages/{source_page_id}', headers={'Authorization': f'Bearer {access_token}'})

        # Get the content of the source page
        page_body = response.json()['body']

        # Create a new page in the destination course using the content of the source page
        new_page_params = {'wiki_page': {'title': dest_page_title, 'body': page_body}}
        response = requests.post(f'{base_url}/courses/{destination_course_id}/pages', headers={'Authorization': f'Bearer {access_token}'}, json=new_page_params)
        if response.status_code != 200:
            raise Exception()
        
        new_page_id = response.json()['url'].split('/')[-1]

        if copy_into_new_module:
            # Create a new module in the destination course
            new_module_params = {'module': {'name': new_module_name, 'position': 1}}
            response = requests.post(f'{base_url}/courses/{destination_course_id}/modules', headers={'Authorization': f'Bearer {access_token}'}, json=new_module_params)
            if response.status_code != 200:
                requests.delete(f'{base_url}/courses/{destination_course_id}/pages/{new_page_id}', headers={'Authorization': f'Bearer {access_token}'})
                raise Exception()
            
            new_module_id = response.json()['id']

            # Add the new page to the new module
            new_item_params = {'module_item': {'title': dest_page_title, 'type': 'Page', 'page_url': new_page_id, 'position': 1}}
            response = requests.post(f'{base_url}/courses/{destination_course_id}/modules/{new_module_id}/items', headers={'Authorization': f'Bearer {access_token}'}, json=new_item_params)
            if response.status_code != 200:
                requests.delete(f'{base_url}/courses/{destination_course_id}/pages/{new_page_id}', headers={'Authorization': f'Bearer {access_token}'})
                requests.delete(f'{base_url}/courses/{destination_course_id}/modules/{new_module_id}', headers={'Authorization': f'Bearer {access_token}'})
                raise Exception()
        
        print(f"Duplicated page for {destination_course_id}")
    except:
        print(f"Failed to duplicate page for {destination_course_id}")


print("Done!")