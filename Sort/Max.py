n1 = [6, 10, 2]
n2 = [3, 30, 34, 5, 9]


# def solution(numbers):
#     answer = ''
#     zero = []
#     for i in range(len(numbers)):
#         print(list(str(numbers[i])), end=' ')
#         zero.append([list(str(numbers[i])), i])
#     print("")
#     print(zero)
#     zero.sort(key=lambda x: (x[0], x[1], x[2], x[3]), reverse=True)
#     result = []
#     for i in zero:
#         result.append(str(numbers[i[1]]))
#     answer = ''.join(result)
#     return answer

def solution(numbers):
    answer = ''

    for i in numbers:
        if len(i)==1:
            pass
        elif len(i)==2:
            pass
        elif len(i)==3:
            pass
        elif len(i)==4:
            pass

    return answer


print(solution(n2))
