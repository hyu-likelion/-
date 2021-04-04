def solution(phone_book):
    answer = True
    hash = {phone: True for phone in phone_book}
    for phone in phone_book:
        stack = ""
        for number in phone[:-1]:
            stack += number
            if stack in hash:
                return False
        
    return answer
