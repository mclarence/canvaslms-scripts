import os
import canvasapi
from config import access_token, base_url

# [[course_id, quiz_id]]
quiz_ids = [
    [23356,64968],
[23369,64969],
[23378,64970],
[23384,64971],
[23414,64972],
[23401,64973],
[23402,64974],
[23403,64975],
[23433,64976],
[23435,64977],
]
canvas = canvasapi.Canvas(base_url, access_token);

# delete each quiz in the list
for quiz in quiz_ids:
    course = canvas.get_course(quiz[0]);
    quiz = course.get_quiz(quiz[1]);
    quiz.delete();