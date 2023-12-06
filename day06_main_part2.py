from collections import defaultdict

f = open("day06_input.txt", "r")
t = 0
current_record = 0
for line in f:
    line = line.strip().split(":")
    if line[0] == "Time":
        x = line[-1].replace(" ","")
        t = int(x)
    elif line[0] == "Distance":
        x = line[-1].replace(" ","")
        current_record = int(x)
print(t,current_record)


n = 0
for t1 in range(t+1):
    if t1 == 0:
        d1 = 0
    else:
        d1 = t1 * (t - t1)
    #print(t1,d1)
    if d1 > current_record:
        n += 1
print(n)

