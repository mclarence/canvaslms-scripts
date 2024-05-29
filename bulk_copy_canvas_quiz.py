import canvasapi
import requests
from config import access_token, base_url

source_course_id = ''
source_quiz_id = ''

# [[course_id, module_id], ...]
courses = [[]]
canvas = canvasapi.Canvas(base_url, access_token);

source_course = canvas.get_course(source_course_id);
source_quiz = source_course.get_quiz(source_quiz_id);

# get the source quiz questions
source_quiz_questions = source_quiz.get_questions();

add_to_module = True

# Set the question group parameters.
question_group = {
    'name': 'My Question Group',
    'pick_count': 3,
    'question_points': 0,
    #'assessment_question_bank_id': 000,
}

for course in courses:
    try:
        dest_course = canvas.get_course(course[0]);
        
        # Create a new quiz in the destination course using the content of the source quiz
        new_quiz_params = {
            'title': source_quiz.title,
            'description': source_quiz.description,
            'quiz_type': source_quiz.quiz_type,
            'time_limit': source_quiz.time_limit,
            'shuffle_answers': source_quiz.shuffle_answers,
            'hide_results': source_quiz.hide_results,
            'show_correct_answers': source_quiz.show_correct_answers,
            'show_correct_answers_last_attempt': source_quiz.show_correct_answers_last_attempt,
            'show_correct_answers_at': source_quiz.show_correct_answers_at,
            'hide_correct_answers_at': source_quiz.hide_correct_answers_at,
            'allowed_attempts': source_quiz.allowed_attempts,
            'scoring_policy': source_quiz.scoring_policy,
            'one_question_at_a_time': source_quiz.one_question_at_a_time,
            'cant_go_back': source_quiz.cant_go_back,
            'access_code': source_quiz.access_code,
            'ip_filter': source_quiz.ip_filter,
            'due_at': source_quiz.due_at,
            'lock_at': source_quiz.lock_at,
            'unlock_at': source_quiz.unlock_at,
            'published': False,
            'one_time_results': source_quiz.one_time_results,
            'only_visible_to_overrides': source_quiz.only_visible_to_overrides,
        }

        new_quiz = dest_course.create_quiz(new_quiz_params);

        new_quiz.create_question_group([question_group])

        assoc_params = {
            'rubric_association[rubric_id]': 36844,
            'rubric_association[association_id]': new_quiz.assignment_id,
            'rubric_association[association_type]': 'Assignment',
            'rubric_association[purpose]': 'grading'
        }

        req = requests.post(f"{base_url}/api/v1/courses/{course[0]}/rubric_associations", data=assoc_params, headers={'Authorization': f'Bearer {access_token}'})

        if req.status_code != 200:
            raise Exception(f"Failed to create rubric association: {req.text}")
        
        if add_to_module:
            # Add the new quiz to the module
            new_module_item = {
                'title': source_quiz.title,
                'type': 'Quiz',
                'content_id': new_quiz.id,
                'position': 1,
            }

            dest_module = dest_course.get_module(course[1]);
            dest_module.create_module_item(new_module_item);

        # store the new quiz id in  a csv file
        with open('new_quiz_ids.csv', 'a') as f:
            f.write(f"{course[0]},{new_quiz.id}\n")
        
        print(f"SUCCESS: {course[0]}")
    except Exception as e:
        print(f"FAILED: {course[0]} - {e}")

print("Done!")