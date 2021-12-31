p1=["leo", "kiki", "eden"]
p2=["marina", "josipa", "nikola", "vinko", "filipa"]
p3=["mislav", "stanko", "mislav", "ana"]

c1=["eden", "kiki"]
c2=["josipa", "filipa", "marina", "nikola"]
c3=["stanko", "ana", "mislav"]

def solution(par,com):
    par.sort()
    com.sort()
    for p,c in zip(par,com):
        if p!=c:
            return p
    return par.pop()

print(solution(p1,c1))
print(solution(p2,c2))
print(solution(p3,c3))