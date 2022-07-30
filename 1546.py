import statistics

n = int(input())
scores = map(int,input().split())
scores = list(scores)

max_score = max(scores)
for i,score in enumerate(scores):
    scores[i] = score/max_score*100
    

print(statistics.mean(scores))
