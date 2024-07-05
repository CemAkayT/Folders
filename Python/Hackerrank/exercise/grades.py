#!/Users/cemakay/Python/.venv/bin/python3


def gradingStudents(grades: list) -> list:
    rounded_grades = []
    
    for i in (grades):
        mult = i // 5
        rem = i % 5
        if ((mult+1) * 5) - i < rem and i >=38:
            rounded_grades.append((mult+1) * 5)
    
        elif((mult+1) * 5 - i >= 3):
            rounded_grades.append(i)

        else:
            rounded_grades.append(i)
    return rounded_grades
    
grades = [73,67,38,33]
res = gradingStudents(grades)
print(res)