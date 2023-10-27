import os
import canvasapi
from config import access_token, base_url

# [[course_id, quiz_id]]
quiz_ids = [[]]
canvas = canvasapi.Canvas(base_url, access_token);

# delete each quiz in the list
for quiz in quiz_ids:
    course = canvas.get_course(quiz[0]);
    quiz = course.get_quiz(quiz[1]);
    quiz.delete();