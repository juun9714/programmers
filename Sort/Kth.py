a=[1, 5, 2, 6, 3, 7, 4]	
c=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	


def solution(array, commands):
    answer = []
    for a in commands:
        i=a[0]
        j=a[1]
        k=a[2]
        li=array[i-1:j]
        li.sort()
        answer.append(li[k-1])
    return answer

solution(a,c)