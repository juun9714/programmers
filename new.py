g=["classic", "pop", "classic", "classic"]
p=[500, 600, 150, 800]

def solution(genres, plays):
    answer = []
    g={}
    d={}

    for i in range(len(genres)):
        g[genres[i]]=g.get(genres[i], 0)+plays[i]
        d[genres[i]]=d.get(genres[i],[])+[(plays[i],i)]
    print(g)
    print(d)

    gen_sort=sorted(g.items(), key=lambda x:x[1], reverse=True)
    print(gen_sort)

    for (gen, cnt) in gen_sort:
        d[gen]=sorted(d[gen],key=lambda x:(-x[0], x[1]))
        answer+=[id for (t, id) in d[gen][:2]]
        #list slice index를 2로 설정해도 개수가 1밖에 없으면 1개만 가져오고 만다. 
    
    print(answer)
    return answer

solution(g,p)