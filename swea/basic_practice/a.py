def solution(participant, completion):
    res = []
    
    for person in participant :
        if not(person in completion) :
            res.append(person)   

    return res.join('')
participant = ["leo", "kiki", "eden"]
completion = 	["eden", "kiki"]

print(solution(participant,completion))