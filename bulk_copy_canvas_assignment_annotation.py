import requests
import canvasapi
from config import access_token, base_url
import os

# Set the source course id and assignment id
source_course_id = 22933

# stage 3
#source_assignment_id = 351194

# stage 4
#source_assignment_id = 351334

# stage 5
#source_assignment_id = 351335

# stage 6
source_assignment_id = 351337

# Set new module name
copy_into_new_module = True

#new_module_name = 'Literacy Project - Stage 3'
#new_module_name = 'Literacy Project - Stage 4'
#new_module_name = 'Literacy Project - Stage 5'
new_module_name = 'Literacy Project - Stage 6'


# stage 3
#rubric_id = 76270

# stage 4
#rubric_id = 76271

# stage 5
#rubric_id = 76272

# stage 6
rubric_id = 76273

# List of canavas course ids to copy the assignment to
courses = [
    23427,
    23424,
    23423,
    23445,
    23441,
    23458,
    23403,
    23433,
    23435,
    23420,
    23457,
    23443,
    23447,
    23404,
    23425,
    23455,
    23421,
    23452,
    23422,
    23449,
    23450,
    23439,
    23454,
    23442,
    23453,
    23440,
    23426,
    22191,
    22192,
    22193,
    22194,
    22195,
    22196,
    22197,
    22198,
    22199,
    22200,
    22201,
    22202,
    22203,
    22204,
    22205,
    23784,
    22206,
    22190,
    22207,
    23200,
    22208,
    22209,
    22210,
    22211,
    22212,
    22213,
    22214,
    22215,
    22216,
    22217,
    24602,
    24525,
    24564,
]

canvas = canvasapi.Canvas(base_url, access_token)

#template_file_path = os.path.join('./writing_sample_templates/', 'stage_3.pdf')
#template_file_path = os.path.join('./writing_sample_templates/', 'stage_4.pdf')
#template_file_path = os.path.join('./writing_sample_templates/', 'stage_5.pdf')
template_file_path = os.path.join('./writing_sample_templates/', 'stage_6.pdf')

base_url = base_url + '/api/v1'

for destination_course_id in courses:
    try:
        course = canvas.get_course(destination_course_id)

        uploaded_file = course.upload(template_file_path)

        assignment_group = course.create_assignment_group(
            name='Literacy Project',
            position=1,
            group_weight=0
        )

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


        assignment_name = assignment_data['name']

        new_assignment_params = {
            'assignment': {
                'name': assignment_name,
                'description': assignment_data['description'],
                'points_possible': assignment_data['points_possible'],
                'grading_type': assignment_data['grading_type'],
                'due_at': assignment_data['due_at'],
                'lock_at': assignment_data['lock_at'],
                'unlock_at': assignment_data['unlock_at'],
                'assignment_group_id': assignment_data['assignment_group_id'],
                'published': False,
                'submission_types': 'student_annotation',
                'annotatable_attachment_id': uploaded_file[1]['id'],
                'omit_from_final_grade': assignment_data['omit_from_final_grade'],
                'assignment_group_id': assignment_group.id,
            }
        }
        

        response = requests.post(f'{base_url}/courses/{destination_course_id}/assignments',
                                headers={'Authorization': f'Bearer {access_token}'},
                                json=new_assignment_params)
        if response.status_code not in [200, 201]:
            raise Exception(response.json())

        new_assignment_id = response.json()['id']

        assoc_params = {
            'rubric_association[rubric_id]': rubric_id,
            'rubric_association[association_id]': new_assignment_id,
            'rubric_association[association_type]': 'Assignment',
            'rubric_association[purpose]': 'grading'
        }

        response = requests.post(f'{base_url}/courses/{destination_course_id}/rubric_associations',
                                headers={'Authorization': f'Bearer {access_token}'},
                                data=assoc_params)
        
        if response.status_code not in [200, 201]:
            raise Exception(response.json())
        

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