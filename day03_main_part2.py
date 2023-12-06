from collections import defaultdict
list_main = []
decode = []
f = open("day03_input.txt", "r")

dict_numbers = defaultdict(list)
for i,line in enumerate(f):
    is_digit = [abc.isdigit() for abc in line.strip()]
    nums_ = [abc for abc in line.strip()]
    list_main.append(nums_)

    nums_final = []
    nums_index = []
    l1 = []
    l2 = []
    for iii,x in enumerate(is_digit):
        if x:
            l1.append(nums_[iii])
            l2.append([i,iii])
            if iii == len(is_digit)-1:
                nums_final.append(l1)
                nums_index.append(l2)
        else:
            if l1:
                nums_final.append(l1)
                nums_index.append(l2)
                l1 = []
                l2 = []

    for j,n in enumerate(nums_final):
        dict_numbers[str(i)+"-"+str(j)+"-"+"".join(n)] += nums_index[j]


list_hits = []
l = []
for i,x in enumerate(list_main):
    for ii,xx in enumerate(x):
        if xx == "*":
            if i - 1 >= 0:
                l.append([i - 1,ii])
            if i - 1 >= 0 and ii - 1 >= 0:
                l.append([i - 1,ii - 1])
            if i - 1 >= 0 and ii + 1 >= 0:
                l.append([i - 1,ii + 1])
            if i + 1 >= 0:
                l.append([i + 1,ii])
            if i + 1 >= 0 and ii - 1 >= 0:
                l.append([i + 1,ii - 1])
            if i + 1 >= 0 and ii + 1 >= 0:
                l.append([i + 1,ii + 1])
            if ii - 1 >= 0:
                l.append([i,ii - 1])
            if ii + 1 >= 0:
                l.append([i,ii + 1])
            list_hits.append(l)
            l = []
print(list_hits)


gears = []
l = []
for pair_hits in list_hits:
    for pair in pair_hits:
        for num in dict_numbers:
            for x in dict_numbers[num]:
                if pair == x:
                    v = num.split("-")
                    l.append(int(v[-1]))
    gears.append(l)
    l = []

print(gears)
sum_ = 0
for x in gears:
    x = list(set(x))
    if len(x) == 2:
        sum_ += (x[0] * x[-1])
print(sum_)
