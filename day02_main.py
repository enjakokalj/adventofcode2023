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

dict_final = defaultdict(list)
test = {"red": 12,"green": 13,"blue": 14}
for n in games:
    for color in games[n]:
        dict_final[n].append(max(games[n][color]) <= test[color])
print(dict_final)

n1 = 0
for n in dict_final:
    if all(dict_final[n]):
        n1 += n
print(n1)

