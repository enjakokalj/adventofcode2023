from collections import defaultdict
f = open("day04_input.txt", "r")

dict_win = defaultdict(list)
dict_nums = defaultdict(list)
for i,line in enumerate(f):
    line = line.strip().split(":")
    card = int(line[0].strip().split(" ")[-1])
    vals = line[-1].split("|")
    win_vals = [int(x) for x in vals[0].strip().split(" ") if x != ""]
    my_vals = [int(x) for x in vals[-1].strip().split(" ") if x != ""]
    dict_win[card] += win_vals
    dict_nums[card] += my_vals

n_all = 0
for i in dict_win:
    x = set(dict_win[i]).intersection(set(dict_nums[i]))
    n = 0
    for ii,_ in enumerate(x):
        if ii == 0:
            n += 1
        else:
            n *= 2
    n_all += n
    print(n,n_all)
print(n_all)
