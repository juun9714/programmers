c=[0, 0]

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        h=i+1
        flag=True
        if h==0:
            return answer
        elif h==len(citations):
            for j in range(h):
                if citations[j]<h:
                    flag=False
                    break
        elif h<len(citations) and citations[h]<h:
            for j in range(h):
                if citations[j]<h:
                    flag=False
                    break
        
        if flag==True:
            answer=h
    return answer

print(solution(c))