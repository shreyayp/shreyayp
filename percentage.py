f __name__ == '__main__':
    n = int(input())  
    student_marks = {}  

    
    for _ in range(n):
        line = input().split()
        name, marks = line[0], line[1:]
        student_marks[name] = list(map(float, marks))

    query_name = input() 
    
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])

   
    print(f"{average_score:.2f}")