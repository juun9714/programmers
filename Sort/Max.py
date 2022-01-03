n1 = [6, 10, 2]
n2 = [3, 30, 34, 5, 9]

def solution(numbers):
    answer = ''
    if numbers.count(0)==len(numbers):
        answer='0'
        return answer
    tmp=[str(x) for x in numbers]
    tmp.sort(key=lambda x:x*4, reverse=True)
    answer=''.join(tmp)
    return answer

print(solution(n2))
