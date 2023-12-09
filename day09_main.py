from collections import defaultdict
f = open("day09_input.txt", "r")

def rec(values):
    values_diff = []
    for i in range(len(values)):
        if i + 1 <= len(values) - 1:
            values_diff.append(values[i + 1] - values[i])
    return values_diff


values_all = []
for line in f:
    values_all.append([int(x) for x in line.strip().split(" ")])


dict_values = defaultdict(list)
for i,values in enumerate(values_all):
    dict_values[i].append(values)
    all_zero = False
    while not all_zero:
        values_diff = rec(values)
        dict_values[i].append(values_diff)
        if all([x == 0 for x in values_diff]):
            #print(dict_values[i])
            all_zero = True
        else:
            values = values_diff


for i in dict_values:
    for ii in [*range(len(dict_values[i]))][::-1]:
        if ii == len(dict_values[i])-1:
            dict_values[i][ii].append(0)
        else:
            dict_values[i][ii].append(dict_values[i][ii][-1] + dict_values[i][ii+1][-1])

print(sum(dict_values[i][0][-1] for i in dict_values))

