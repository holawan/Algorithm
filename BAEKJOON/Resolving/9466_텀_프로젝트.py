import sys 

T = int(sys.stdin.readline())
for t in range(T) :

    n = int(sys.stdin.readline())

    students = [i for i in range(1,n+1)]
    pick_lst = list(map(int,sys.stdin.readline().split()))
    
    team  = set()
    for student in students :
        if not student in team :
            first = student
            tmp  = [first]  
            while True :
                pick = pick_lst[student-1]
                if pick in team : 
                    break 
                tmp.append(pick)
                if student == pick :
                    team.add(pick)
                    break 
                elif first == pick :
                    for t in tmp :
                        team.add(t)
                    break
                student = pick 
    
    print(n-len(team))
    

