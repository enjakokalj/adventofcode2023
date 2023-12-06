from collections import defaultdict

#part1
dict_ = defaultdict(list)

f = open("day01_input.txt", "r")
for i,line in enumerate(f):
    #print(line)
    for a in line:
        if a.isdigit():
            dict_[i].append(a)
#print(dict_)

list_final = []
for x in dict_:
    list_final.append(int(dict_[x][0]+dict_[x][-1]))
#print(list_final)
print("part1:",sum(list_final))



#part2
def rec(text,to_find,prev=0):
    list_ = []
    x = text.find(to_find)
    if x != -1:
        val = x+prev
        list_.append(val)
        text_new = text[(x+len(to_find)):]
        prev_new = val+len(to_find)
        list_ += rec(text_new,to_find,prev_new)
        return list_
    if x == -1:
        return list_


dict_ = defaultdict(list)

keys = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

f = open("day01_input.txt", "r")
list_info = []
list_final = []
for i,line in enumerate(f):
    for ii,a in enumerate(line):
        if a.isdigit():
            dict_[i].append([ii,a])
    for n in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
        index = rec(line,n)
        for iii in index:
            dict_[i].append([iii,keys[n]])

    dict_[i] = sorted(dict_[i])

    x1 = dict_[i][0][-1]
    if x1 in keys:
        x1 = keys[x1]
    x2 = dict_[i][-1][-1]
    if x2 in keys:
        x2 = keys[x2]
    xxx = (int(str(x1) + str(x2)))

    #print(line,dict_[i],xxx)
    list_info.append([line,dict_[i],xxx])
    list_final.append(xxx)

print("part2:",sum(list_final))
