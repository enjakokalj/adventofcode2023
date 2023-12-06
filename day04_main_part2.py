from tqdm import tqdm
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

dict_ic = defaultdict(int)
for i in dict_win:
    x = len(set(dict_win[i]).intersection(set(dict_nums[i])))
    dict_ic[i] = x

dict_to_add = defaultdict(list)
for i in dict_ic:
    ic = i
    for iii in range(dict_ic[i]):
        ic += 1
        dict_to_add[i].append(ic)


won_final = []
won_next = [i for i in dict_win]
while won_next:
    next = []
    won_final += won_next
    for i in tqdm(won_next):
        next += dict_to_add[i]
    won_next = next

dict_won = defaultdict(int)
for x in won_final:
    dict_won[x] += 1
print(dict_won)

print(sum(dict_won.values()))

