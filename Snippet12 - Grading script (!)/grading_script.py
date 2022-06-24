# >>>>>>> For testing purposes <<<<<<<
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }

student_scores = {}

wish_to_continue = True
while wish_to_continue:
    student_name = str(input("Type in student name:"))
    student_score = int(input("Type in student score (1 to 100):"))
    student_scores[student_name] = student_score
    ask_to_continue = str(input(
        'Do you wish to continue? Hit enter to continue or type "no" to end')).lower()
    if ask_to_continue == "no":
        wish_to_continue = False

student_grades = {}

ranges = {
    range(0, 71): "Fail",
    range(71, 81): "Acceptable",
    range(81, 91): "Exceeds Expectations",
    range(91, 101): "Outstanding",
}

for student in student_scores:
    end_of_loop = False
    if student_scores[student] not in range(0, 101):
        end_of_loop = True
        print(f"{student}'s score out of range")
    while not end_of_loop:
        for grade in ranges:
            if student_scores[student] in grade:
                student_grades[student] = ranges[grade]
                end_of_loop = True

for student in student_grades:
    print(f"{student}: {student_grades[student]}")
