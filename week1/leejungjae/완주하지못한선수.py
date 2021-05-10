def solution(participant, completion):
    hastTable = {}
    
    # 테이블 생성
    for i in range(len(completion)):
        
        print(i,completion[i],hastTable)
        
        # 이미 존재한다면 +1
        if completion[i] in hastTable:
            hastTable[completion[i]] =  hastTable[completion[i]] + 1
            
        # 존재하지 않는다면 딕셔너리에 등록
        else : 
            hastTable[completion[i]] = 1
    
    print(hastTable)
    # retIdx = 0
        
    # # 검증
    # for i in range(len(participant)):
        
    #     # 테이블에 존재한다면 숫자 감소
    #     if participant[i] in hastTable and hastTable[participant[i]] > 0: 
    #         hastTable[participant[i]] = hastTable[participant[i]] - 1
    #     # 존재하지 않는다면 해당 선수가 완주 못함
    #     else :
    #         retIdx = i
    #         break
            
    # return participant[retIdx]

solution([],['kiki','kiki','kiki','kiki','kiki','jj','www'])