pb1=["119", "97674223", "1195524421"]
pb2=["123","456","789"]
pb3=["12","123","1235","567","88"]
#있으면 false,

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        j=i+1
        while j<len(phone_book):
            one=phone_book[i]
            two=phone_book[j]
            if two.startswith(one):
                answer=False
                return answer
            elif two>one:
                break
            j=j+1
    
    return answer

print(solution(pb2))