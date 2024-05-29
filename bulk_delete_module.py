import os
import canvasapi
from config import access_token, base_url

# [[course_id, module_id]]
module_id = [
    [23356,88167],
[23369,88168],
[23378,88169],
[23384,88170],
[23414,88171],
[23401,88172],
[23402,88173],
[23403,88174],
[23433,88175],
[23435,88176],
]

canvas = canvasapi.Canvas(base_url, access_token);

for module in module_id:
    course = canvas.get_course(module[0]);
    module = course.get_module(module[1]);
    module.delete();