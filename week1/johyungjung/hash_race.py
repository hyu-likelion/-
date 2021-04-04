def solution(participant, completion):
    candidates = {person: 0 for person in participant}
    for person in participant:
        candidates[person] += 1
    for person in completion:
        candidates[person] -= 1
    answer = ""
    for key, val in candidates.items():
        if val > 0:
            answer = key
    
    return answer
