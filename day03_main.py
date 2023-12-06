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
for i,x in enumerate(list_main):
    for ii,xx in enumerate(x):
        if not xx.isdigit() and xx != ".":
            if i - 1 >= 0:
                list_hits.append([i - 1,ii])
            if i - 1 >= 0 and ii - 1 >= 0:
                list_hits.append([i - 1,ii - 1])
            if i - 1 >= 0 and ii + 1 >= 0:
                list_hits.append([i - 1,ii + 1])
            if i + 1 >= 0:
                list_hits.append([i + 1,ii])
            if i + 1 >= 0 and ii - 1 >= 0:
                list_hits.append([i + 1,ii - 1])
            if i + 1 >= 0 and ii + 1 >= 0:
                list_hits.append([i + 1,ii + 1])
            if ii - 1 >= 0:
                list_hits.append([i,ii - 1])
            if ii + 1 >= 0:
                list_hits.append([i,ii + 1])
#print(list_hits)


sum_n = 0
for num in dict_numbers:
    if sum([pair in list_hits for pair in dict_numbers[num]]) != 0:
        v = num.split("-")
        sum_n += int(v[-1])
        #print(num)

print(sum_n)

