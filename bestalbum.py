g=["classic", "pop", "classic", "classic", "pop"]
p=[500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    gen_tot={}
    d={}

    for i in range(len(genres)):
        gen_tot[genres[i]]=gen_tot.get(genres[i],0)+plays[i]
        d[genres[i]]=d.get(genres[i],[])+[(plays[i],i)]

    gen_sort=sorted(gen_tot.items(), key=lambda x:x[1], reverse=True)
    for (genre, cnt) in gen_sort:
        d[genre]=sorted(d[genre], key=lambda x:(-x[0], x[1]))
        answer+=[idx for (play, idx) in d[genre][:2]]
        #list slice index를 2로 설정해도 개수가 1밖에 없으면 1개만 가져오고 만다. 

    return answer

print(solution(g,p))