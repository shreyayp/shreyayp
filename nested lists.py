if __name__ == '__main__':
    n = int(input())  
    students = []  

    
    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])

    
    unique_grades = sorted(set(grade for name, grade in students))

   
    second_lowest_grade = unique_grades[1]

   
    sec_student_names = [name for name, grade in students if grade == second_lowest_grade]
    sec_student_names.sort()  

    
    for name in sec_student_names:
        print(name)
