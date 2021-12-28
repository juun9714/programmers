g=["classic", "pop", "classic", "classic", "pop"]
p=[500, 600, 150, 800, 2500]

def solution(genres, plays):
    tot={}
    for i in range(len(genres)):
        if genres[i] not in tot:
            tot[genres[i]]=plays[i]
        else:
            tot[genres[i]]+=plays[i]

    print(max(tot.values()))

    answer = []
    return answer

solution(g,p)