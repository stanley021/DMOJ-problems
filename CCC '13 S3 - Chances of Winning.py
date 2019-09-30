import copy as copy
t = int(input())
g = int(input())
scores = [0 for n in range(5)]
teams = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
wins = 0

for n in range(g):
    a,b,sa,sb = map(int,input().split())
    for y in teams:
        if y[0] == a and y[1] == b:
            teams.remove([a,b])
    if sa > sb:
        scores[a] += 3
    elif sb > sa:
        scores[b] += 3
    elif sb == sa:
        scores[b] += 1
        scores[a] += 1

def dfs(scores,teams):
    global wins
    if len(teams) == 0:
        fav_score = scores[t]
        for x in range(1,5):
            if scores[x] >= fav_score and t!=x:
                return
        wins += 1
        return
    else:
        temp_games = copy.deepcopy(teams)
        temp_games.pop(0)
        n = teams[0]
        for x in range(3):
            temp_score = copy.copy(scores)
            if x == 0:
                temp_score[n[0]] +=3
            elif x == 1:
                temp_score[n[1]] += 3
            elif x == 2:
                temp_score[n[1]] += 1
                temp_score[n[0]] += 1
            dfs(temp_score,temp_games)
dfs(scores,teams)
print(wins)
