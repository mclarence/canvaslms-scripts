import canvasapi
from config import access_token, base_url

canvas = canvasapi.Canvas(base_url, access_token);

NEW_IMAGES = {
    "GIVE_1": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Give%201.gif?raw=true",
    "GIVE_2": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Give%202.gif?raw=true",
    "GIVE_3": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Give%203.gif?raw=true",
    "SEEK_1": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Seek1.gif?raw=true",
    "SEEK_2": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Seek%202.gif?raw=true",
    "SEEK_3": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Seek%203.gif?raw=true",
    "USE_1": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Use%201.gif?raw=true",
    "USE_2": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Use%202.gif?raw=true",
    "USE_3": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Use%203.gif?raw=true",
    "JAMBOARD": "https://github.com/Santa-Sophia-Catholic-College/canvas-shared-assets/blob/main/learner-agency/Jamboard_Logo.png?raw=true",
}

OLD_IMAGES = {
    "GIVE_1": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaCEuws41zh99W2s1UiRPZLlVM20iKDBIzL5PgpDbZwv6lEghn9Ib1tfFrbXOti1Ww6qv24RGqDX4kwzeDUFdaFmiP05ag=s1600",
    "GIVE_2": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaDy3fDrNBTSd4gMUG7aCV3xRndW6EFDvklIGAchyAUii6w1S2VGsoIjThh3GR7iStZM5ZN4FjFPCEb_6RKMOH7thdg5=s1600",
    "GIVE_3": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaBKacciB_o8OrQXNreB-8IiZ6el9sFtuIlh20uhhkMozyC-Ip43N_Hb8UPUwIOufxYqhJKRwJtaZiDU2irWu0q2USlEvA=s1600",
    "SEEK_1": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaBTC2Xu7vo-90wZeg0TMp7aiBWPZHj4ksVlP64nzhNlQyLSf4lF9wjuJxWUwQREKGJfqU1-QXBYXms6P0gbw4zgJHEqGA=s1600",
    "SEEK_2": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaB2eMiJt_sz9-vdUP8BqxqwUQ1z4s5nOAV6WzpB1FWfs6y5p19H74peT39UIwxnXPoE2a11FTDgLF54bSjqdXtjrJQ9uA=s1600",
    "SEEK_3": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaAvx_T6CZGlpxOrw8-ZLmWA-ro8BpbWfTeowBO2VWtxQxqR1wBDJDl9QIS9z-vrSCH5RxudG1ScO2LICx-UTSl6yFQ9-A=s1600",
    "USE_1": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaCcEShFKv7QaGWiY0ANwjOzFtRL_uLTTFaBu7uK0LS8mVB6b2ijlvVt3vsVJ8A4Yh4goNJTpDa1887Dj6Ujs7lX4JP-Bw=s1600",
    "USE_2": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaBUK27s_C1FWC0OeUnUC-BlAGLkOWr61MA2xSa2-NiK9ntUYIOkNR63z8NRNm4G0k2PdXyxul-cjik3X4M4MJcrre91=s1600",
    "USE_3": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaArMS4dhksN6NJEOx60apBESx6pPBaMf1gABoJANUI_XPZwxX4-00p3-LHu2aVvgTvve5ojMA96CFP4TUFIo4_UfYKzhw=s1600",
    "JAMBOARD": "https://lh3.googleusercontent.com/drive-viewer/AK7aPaA6aZ_mK2xoZyDA_dMYouK5XiOVTRHvq_410k9uXXm-XRzzWBgX7TVFjxl41DK1iPb-zW-8fbIus3X-b7sQg7wk5Nmhwg=s1600",
}

COURSE_QUIZ_PAIRS = [
    [20043,55538],
    [20045,55539],
    [20054,55540],
    [20057,55541],
    [20074,55542],
    [19995,55543],
    [20065,55544],
    [20091,55545],
    [20092,55546],
    [20093,55547],
    [21190,55548],
    [20008,55549],
    [20066,55550],
    [20062,55551],
    [20096,55552],
    [20078,55553],
    [20099,55554],
    [20100,55555],
    [20009,55556],
    [20071,55557],
    [20081,55558],
    [22320,55559]
]

for course_id, quiz_id in COURSE_QUIZ_PAIRS:
    course = canvas.get_course(course_id)
    quiz = course.get_quiz(quiz_id)
    
    quiz.description = quiz.description.replace(OLD_IMAGES["GIVE_1"], NEW_IMAGES["GIVE_1"])
    quiz.description = quiz.description.replace(OLD_IMAGES["GIVE_2"], NEW_IMAGES["GIVE_2"])
    quiz.description = quiz.description.replace(OLD_IMAGES["GIVE_3"], NEW_IMAGES["GIVE_3"])
    quiz.description = quiz.description.replace(OLD_IMAGES["SEEK_1"], NEW_IMAGES["SEEK_1"])
    quiz.description = quiz.description.replace(OLD_IMAGES["SEEK_2"], NEW_IMAGES["SEEK_2"])
    quiz.description = quiz.description.replace(OLD_IMAGES["SEEK_3"], NEW_IMAGES["SEEK_3"])
    quiz.description = quiz.description.replace(OLD_IMAGES["USE_1"], NEW_IMAGES["USE_1"])
    quiz.description = quiz.description.replace(OLD_IMAGES["USE_2"], NEW_IMAGES["USE_2"])
    quiz.description = quiz.description.replace(OLD_IMAGES["USE_3"], NEW_IMAGES["USE_3"])
    quiz.description = quiz.description.replace(OLD_IMAGES["JAMBOARD"], NEW_IMAGES["JAMBOARD"])

    quiz.edit(quiz={"description": quiz.description})
    print("Updated quiz: " + quiz.title)