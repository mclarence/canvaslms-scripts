import os
from config import access_token, base_url
from canvasapi import Canvas


canvas = Canvas(base_url, access_token)

course_ids = [
    23361,
    23371,
    23358,
    23363,
    23365,
    23357,
    23366,
    23370,
    23364,
    24678,
    23367,
    23356,
    23362,
    23372,
    23369,
    23353,
    23368,
    23354,
    24677,
    23359,
    23360,
]

for course_id in course_ids:
    try:
        course = canvas.get_course(course_id)

        # get course folders
        folders = course.get_folders()

        course_images_folder = None
        for folder in folders:
            if folder.name == "course_images":
                course_images_folder = folder
                break

        if course_images_folder is None:
            course_images_folder = course.create_folder("course_images")

        # upload the files to the course_images folder
        for file in os.listdir("course_images"):
            file_path = os.path.join("course_images", file)
            course_images_folder.upload(file_path)
        
        print("Uploaded files to course_images folder in course " + str(course_id))
    except Exception as e:
        print("Error uploading files to course_images folder in course " + str(course_id))
        print(e)