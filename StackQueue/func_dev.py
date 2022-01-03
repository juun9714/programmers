p1=[93, 30, 55]
p2=[95, 90, 99, 99, 80, 99]	
s1=[1, 30, 5]
s2=[1, 1, 1, 1, 1, 1]	


def solution(progresses, speeds):
    class work:
        prog=0
        speed=0
        done=False
         
        def __init__(self, p, s, d):
            self.prog=p
            self.speed=s
            self.done=d

    answer = []
    li=[]
    
    for i in range(len(progresses)):
        li.append(work(progresses[i], speeds[i], False))

    time=0

    while len(li)>0 and time<100:
        # print("[Time "+str(time)+"]")
        # for i in range(len(li)):
        #     print(li[i].prog, li[i].done)
            
        ret=0
        for i in range(len(li)):
            li[i].prog+=li[i].speed
            if li[i].prog>=100:
                li[i].done=True 

        while len(li)>0 and li[0].done==True:
            li.pop(0)
            ret+=1
        #print("returned work : "+ str(ret))

        if ret!=0:
            answer.append(ret)
        time+=1
    return answer


# print(solution(p1,s1))
print(solution(p2,s2))