list_of_student_subjects = []
for student in range(5):
    subject = input('Enter a list of four school subjects separated with comma: ').replace(' ', '').lower().split(",")
    list_of_student_subjects.extend(subject)
# print(list_of_student_subjects)

set_of_subjects = set(list_of_student_subjects)
# print(set_of_subjects)

dict_of_subjects = dict.fromkeys(set_of_subjects, 0)
# print(dict_of_subjects)

for subject in set_of_subjects:
    values = list_of_student_subjects.count(subject)
    dict_of_subjects[subject] = values
print(dict_of_subjects)

max_val = max(dict_of_subjects, key=dict_of_subjects.get)
print(f'The most common subject is {max_val}')







