from collections import defaultdict
f = open("day02_input.txt", "r")
games = {}

for line in f:
    x1,x2 = line.split(":")
    n = int(x1.split(" ")[-1])
    g = x2.strip().split(";")
    dict_ = defaultdict(list)
    for gg in g:
        gg = gg.split(",")
        for ggg in gg:
            ggg = ggg.strip().split(" ")
            dict_[ggg[-1]].append(int(ggg[0]))
    games[n] = dict_
print(games)


games_min = {n: {x: max(games[n][x]) for x in games[n]} for n in games}
print(games_min)

list_final = []
n2 = 1
for n in games_min:
    for x in games_min[n].values():
        n2 *= x
    list_final.append(n2)
    n2 = 1
print(list_final)
print(sum(list_final))
