c1=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
c2=[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

#dictionary 활용하기 
#dictionary 값은 수정 가능, tuple은 값 수정 불가

def solution(clothes):
    cnt_dict={}
    answer = 1

    for i in clothes:
        if i[1] in cnt_dict:
            cnt_dict[i[1]]+=1
        else:
            cnt_dict[i[1]]=1

    for j in cnt_dict.values():
        answer*=j+1 #안입은 경우 + 개수
    
    return (answer-1)

print(solution(c2))