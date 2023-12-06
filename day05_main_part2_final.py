from collections import defaultdict
from tqdm import tqdm

f = open("day05_input.txt", "r")
seeds = []

lists = [[],[],[],[],[],[],[]]

ii = 0
for line in f:
    #print(line)
    if line != "\n":
        line = line.strip().split(":")
        if line[0] in ("seeds"
                       ,"seed-to-soil map"
                       ,"soil-to-fertilizer map"
                       ,"fertilizer-to-water map"
                       ,"water-to-light map"
                       ,"light-to-temperature map"
                       ,"temperature-to-humidity map"
                       ,"humidity-to-location map"):
            ii += 1
            if ii == 1:
                seeds += [int(x) for x in line[-1].strip().split(" ")]
        else:  # destination range start, the source range start, and the range length
            line = [int(x) for x in line[0].split(" ")]
            destination = line[0]
            source = line[1]
            lists[ii-2].append([line[1],line[0],line[-1]])


#the closest location that needs a seed
#the lowest location number that corresponds to any of the initial seeds

def check_len(mod_range2,sum_range,):
    all_n = sum(xx[1] - xx[0] for xx in mod_range2)
    return all_n == sum_range


def get_mod_range(x,range_):
    mod_range_i = []
    mod_range = []
    for _ in range(len(range_)):
        mod_range_i.append(0)
    for i,r in enumerate(range_):
        a,b = r
        sum_range = b-a
        mod_range2 = []
        for xx in lists[x]:
            src1,d,r = xx
            src2 = src1 + r
            if src2 < a or src1 > b:
                pass
            elif src1 < a < src2 < b:
                mod_range.append((a+d-src1,src2+d-src1))
                mod_range2.append((a,src2))
                mod_range_i[i] += 1
                if check_len(mod_range2,sum_range):
                    break
            elif a < src1 < b < src2:
                mod_range.append((src1+d-src1,b+d-src1))
                mod_range2.append((src1,b))
                mod_range_i[i] += 1
                if check_len(mod_range2,sum_range):
                    break
            elif src1 < a < b < src2:
                mod_range.append((a+d-src1,b+d-src1))
                mod_range2.append((a,b))
                mod_range_i[i] += 1
                if check_len(mod_range2,sum_range):
                    break
            elif a < src1 < src2 < b:
                mod_range.append((src1+d-src1,src2+d-src1))
                mod_range2.append((src1,src2))
                mod_range_i[i] += 1
                if check_len(mod_range2,sum_range):
                    break
            elif src1 < src2 == a < b:
                mod_range.append((a + d - src1,a + 1 + d - src1))
                mod_range2.append((a,a + 1))
                mod_range_i[i] += 1
                if check_len(mod_range2,sum_range):
                    break
            elif a < b == src1 < src2:
                mod_range.append((b + d - src1,b + 1 + d - src1))
                mod_range2.append((b,b + 1))
                mod_range_i[i] += 1
                if check_len(mod_range2,sum_range):
                    break
            elif (a == src1 < src2 < b) or (a < src1 < src2 == b):
                mod_range.append((src1 + d - src1,src2 + d - src1))
                mod_range2.append((src1,src2))
                mod_range_i[i] += 1
                if check_len(mod_range2,sum_range):
                    break
            elif (a == src1 < b < src2) or (src1 < a < b == src2):
                mod_range.append((a + d - src1,b + d - src1))
                mod_range2.append((a,b))
                mod_range_i[i] += 1
                if check_len(mod_range2,sum_range):
                    break

        if mod_range_i[i] == 0:
            mod_range.append(range_[i])

        all_n = sum(xx[1] - xx[0] for xx in mod_range2)
        if mod_range_i[i] != 0 and all_n != sum_range:
            mod_range2.sort(key=lambda z: z[0])
            if len(mod_range2) == 1:
                c,d = mod_range2[0][0],mod_range2[0][1]
                if a == c:
                    mod_range.append((d,b))
                elif b == d:
                    mod_range.append((a,c))
                elif a < c < d < b:
                    mod_range.append((a,c))
                    mod_range.append((d,b))
                else:
                    print("dodatne možnosti - za popravit #1",mod_range)
            else:
                for ir in range(len(mod_range2)):
                    brr = mod_range2[ir][1]
                    if ir == len(mod_range2)-1:
                        if brr != b:
                            mod_range.append((mod_range2[ir][1],b))
                    else:
                        try:
                            ar,br = mod_range2[ir][1],mod_range2[ir+1][0]
                        except IndexError:
                            ir += 2
                        if ir == 0 and mod_range2[ir][0] != a:
                            mod_range.append((a,ar))
                        elif ar == br:
                            pass
                        elif ar != br:
                            mod_range.append((ar,br))
                        else:
                            print("dodatne možnosti - za popravit #2",mod_range)
    return mod_range


#MAIN
min_location = -1
print(seeds)
seeds_pairs = []
for i in range(0,len(seeds),2):
    seeds_pairs.append(seeds[i:i+2])
print(seeds_pairs)
for pair in seeds_pairs:
    s1,s2 = pair
    range_ = [(s1,s1+s2)]
    for x in range(len(lists)):
        range_ = get_mod_range(x,range_)

    #get min_location
    mmm = min(range_)[0]
    if min_location == -1:
        min_location = mmm
    elif mmm < min_location:
        min_location = mmm
print(min_location)

