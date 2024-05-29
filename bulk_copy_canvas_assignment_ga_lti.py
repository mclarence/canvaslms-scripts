import requests
import os
from config import access_token, base_url

# Set the source course id and assignment id
source_course_id = '23384'
source_assignment_id = '348787'

# Set new module name
copy_into_new_module = True
new_module_name = 'My New Module'
# List of canavas course ids to copy the assignment to
courses = [26027]

base_url = base_url + '/api/v1'

for destination_course_id in courses:
    try:

        # get course name
        response = requests.get(f'{base_url}/courses/{destination_course_id}',
                                headers={'Authorization': f'Bearer {access_token}'})
        
        if response.status_code not in [200, 201]:
            raise Exception(response.json())
        
        course_name = response.json()['name']

        # Make a GET request to retrieve the source assignment details
        response = requests.get(f'{base_url}/courses/{source_course_id}/assignments/{source_assignment_id}',
                                headers={'Authorization': f'Bearer {access_token}'})

        # Get the content of the source assignment
        assignment_data = response.json()

        # make a new module
        if copy_into_new_module:
            # Create a new module in the destination course
            new_module_params = {'module': {'name': new_module_name, 'position': 1}}
            response = requests.post(f'{base_url}/courses/{destination_course_id}/modules',
                                    headers={'Authorization': f'Bearer {access_token}'},
                                    json=new_module_params)
            if response.status_code not in [200, 201]:
                raise Exception(response.json())

            new_module_id = response.json()['id']

                # get course sections
        response = requests.get(f'{base_url}/courses/{destination_course_id}/sections',
                                headers={'Authorization': f'Bearer {access_token}'})
        
        if response.status_code not in [200, 201]:
            raise Exception(response.json())
        
        sections = response.json()

        for section in sections:
            if section['name'] != course_name:
                # Create a new assignment in the destination course using the content of the source assignment

                assignment_name = assignment_data['name'] + ' - ' + section['name'].upper()

                new_assignment_params = {
                    'assignment': {
                        'name': assignment_data,
                        'description': assignment_data['description'],
                        'points_possible': assignment_data['points_possible'],
                        'grading_type': assignment_data['grading_type'],
                        'due_at': assignment_data['due_at'],
                        'lock_at': assignment_data['lock_at'],
                        'unlock_at': assignment_data['unlock_at'],
                        'assignment_group_id': assignment_data['assignment_group_id'],
                        'published': False,
                        'submission_types': assignment_data['submission_types'],
                        'omit_from_final_grade': assignment_data['omit_from_final_grade'],
                        'assignment_overrides': [{
                            'course_section_id': section['id'],
                        }],
                        'only_visible_to_overrides': True,
                    }
                }
                

                # check if external_tool_tag_attributes is present in the assignment data
                if 'external_tool_tag_attributes' in assignment_data:
                    new_assignment_params['assignment']['external_tool_tag_attributes'] = assignment_data['external_tool_tag_attributes']

                response = requests.post(f'{base_url}/courses/{destination_course_id}/assignments',
                                        headers={'Authorization': f'Bearer {access_token}'},
                                        json=new_assignment_params)
                if response.status_code not in [200, 201]:
                    raise Exception(response.json())

                new_assignment_id = response.json()['id']

                # Add the new assignment to the new module
                if copy_into_new_module:
                    new_item_params = {'module_item': {'title': assignment_name, 'type': 'Assignment', 'content_id': new_assignment_id, 'position': 1}}
                    response = requests.post(f'{base_url}/courses/{destination_course_id}/modules/{new_module_id}/items',
                                            headers={'Authorization': f'Bearer {access_token}'},
                                            json=new_item_params)
                    if response.status_code not in [200, 201]:                       
                        raise Exception(response.json())

        # store the new module id and the new assignment id in a csv file with the course id
        with open('module_assignment_ids.csv', 'a') as f:
            f.write(f'{destination_course_id},{new_module_id},{new_assignment_id}\n')
                    
        print(f"SUCCESS: {destination_course_id}")
    except Exception as e:
        print(f"FAILED: {destination_course_id} - {e}")

print("Done!")