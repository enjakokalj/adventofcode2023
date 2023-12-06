from collections import defaultdict

f = open("day06_input.txt", "r")
dict_time = defaultdict(int)
dict_distance = defaultdict(int)
for line in f:
    line = line.strip().split(":")
    if line[0] == "Time":
        for i,x in enumerate([x for x in line[-1].strip().split(" ") if x]):
            dict_time[i] = int(x)
    elif line[0] == "Distance":
        for i,x in enumerate([x for x in line[-1].strip().split(" ") if x]):
            dict_distance[i] = int(x)
print(dict_time)
print(dict_distance)


n = []
for i in dict_time:
    n0 = 0
    t = dict_time[i]
    current_record = dict_distance[i]
    for t1 in range(t+1):
        if t1 == 0:
            d1 = 0
        else:
            d1 = t1 * (t - t1)
        #print(t1,d1)
        if d1 > current_record:
            n0 += 1
    n.append(n0)
print(n)
multiply_n = 1
for x in n:
    multiply_n *= x
print(multiply_n)

