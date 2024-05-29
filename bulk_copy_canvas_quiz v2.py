import canvasapi
import requests
import urllib.parse
from config import access_token, base_url

source_course_id = 22933
# 52382 - feedback quiz
# 63953 - purpose quiz
source_quiz_id = 52382
#70671 - feedback rubric
#70670 - purpose rubric
rubric_id = 70671
# [course_id]
courses = [23356, 23369, 23378, 23384, 23414, 23401, 23402, 23403, 23433, 23435]
canvas = canvasapi.Canvas(base_url, access_token);

source_course = canvas.get_course(source_course_id);
source_quiz = source_course.get_quiz(source_quiz_id);

# get the source quiz questions
source_quiz_questions = source_quiz.get_questions();

add_to_module = True
module_name = 'Learner Capabilities - Learner Agency'

for course in courses:
    try:
        dest_course = canvas.get_course(course);
        
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

        source_quiz_questions = source_quiz.get_questions();

        new_quiz = dest_course.create_quiz(new_quiz_params);

        try:
            for source_question in source_quiz_questions:
                # new_quiz.create_question(
                #     question_name=source_question.question_name,
                #     question_text=source_question.question_text,
                #     quiz_group_id=source_question.quiz_group_id,
                #     question_type=source_question.question_type,
                #     position=source_question.position,
                #     points_possible=source_question.points_possible,
                #     correct_comments=source_question.correct_comments,
                #     incorrect_comments=source_question.incorrect_comments,
                #     neutral_comments=source_question.neutral_comments,
                #     answers=source_question.answers,
                # )

                url = f"{base_url}/api/v1/courses/{course}/quizzes/{new_quiz.id}/questions"

                question_params = {
                    'question[question_name]': source_question.question_name,
                    'question[question_text]': source_question.question_text,
                    'question[question_type]': source_question.question_type,
                    'question[points_possible]': source_question.points_possible,
                    # 'question[correct_comments]': source_question.correct_comments,
                    # 'question[incorrect_comments]': source_question.incorrect_comments,
                    # 'question[neutral_comments]': source_question.neutral_comments,
                    # 'question[answers][][text]': source_question.answers[0]['text'],
                    # 'question[answers][][weight]': source_question.answers[0]['weight'],
                }

                for idx, answer in enumerate(source_question.answers):
                    question_params[f'question[answers][{idx}][text]'] = answer['text']
                    question_params[f'question[answers][{idx}][weight]'] = answer['weight']


                req = requests.post(url, data=question_params, headers={'Authorization': f'Bearer {access_token}'})
                if req.status_code != 200:
                    raise Exception(f"Failed to create question: {req.text}")
        except Exception as e:
            print(f"FAILED to create question: {e}")
            # delete the quiz if we failed to create a question
            new_quiz.delete()
            continue
            

        # 70671 - feedback rubric
        # 70670 - purpose rubric
        assoc_params = {
            'rubric_association[rubric_id]': rubric_id,
            'rubric_association[association_id]': new_quiz.assignment_id,
            'rubric_association[association_type]': 'Assignment',
            'rubric_association[purpose]': 'grading'
        }

        req = requests.post(f"{base_url}/api/v1/courses/{course}/rubric_associations", data=assoc_params, headers={'Authorization': f'Bearer {access_token}'})

        if req.status_code != 200:
            # delete the quiz if we failed to create a rubric association
            new_quiz.delete()
            raise Exception(f"Failed to create rubric association: {req.text}")
        
        if add_to_module:
            new_module = dest_course.create_module({
                'name': module_name,
                'position': 1,
            })
            # Add the new quiz to the module
            new_module_item = { 
                'title': source_quiz.title,
                'type': 'Quiz',
                'content_id': new_quiz.id,
                'position': 1,
            }



            #dest_module = dest_course.get_module(course[1]);
            new_module.create_module_item(new_module_item);

        # store the new quiz id in  a csv file
        # course_id, new_quiz_id, module_id
        with open('new_quiz_ids.csv', 'a') as f:
            f.write(f"{course},{new_quiz.id},{new_module.id}\n")
        
        print(f"SUCCESS: {course}")
    except Exception as e:
        print(f"FAILED: {course} - {e}")

print("Done!")