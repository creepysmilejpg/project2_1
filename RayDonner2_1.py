def main():
    scores = list(grade_list())

    for i in range(0, len(scores)):
        scores[i] = int(scores[i])

    scores.sort(reverse=True)
    studentsGrades = len(scores)
    grades_assign(scores, studentsGrades)

    wait = input('\nPress enter to end: ')


def grade_list():
    check = 0
    gradesCount = int(input('Total number of students: '))
    grades = input(f'Enter {gradesCount} grade(s): \n').split()

    for grade in grades: check += 1

    while check != gradesCount:
        check = 0
        grades = input(f'Error: Enter {gradesCount} grade(s): \n').split()
        for grade in grades:
            check += 1

    return grades


def grades_assign(scores, studentScores):
    best = scores[0]
    letterGrade = []
    hold = scores

    for i in range(0, studentScores):
        if scores[i] >= best - 10:
            letterGrade.append('A')
        elif scores[i] >= best - 20:
            letterGrade.append('B')
        elif scores[i] >= best - 30:
            letterGrade.append('C')
        elif scores[i] >= best - 40:
            letterGrade.append('D')
        else:
            letterGrade.append('F')

    for j in range(0, studentScores):
        print(f'Student {j + 1} score is: {hold[j]} and grade is: {letterGrade[j]}')


main()
