from collections import defaultdict
from math import lcm

f = open("day08_input.txt", "r")

instructions = ""
dict_connections = defaultdict(list)
for line in f:
    if line != "\n":
        if "=" not in line:
            instructions = line.strip()
        else:
            dict_connections[line[:3]] += [line[7:10],line[12:15]]

print(instructions)
print(dict_connections)


start_nodes = [x for x in dict_connections if x[-1] == "A"]
n_steps_ = []
for node in start_nodes:
    start_node = node
    goal_reached = False
    n_steps = 0
    while not goal_reached:
        for direction in instructions:
            n_steps += 1
            next_node = dict_connections[node][direction == "R"]
            if next_node[-1] == "Z":
                print(start_node,n_steps)
                n_steps_.append(n_steps)
                goal_reached = True
                break
            else:
                node = next_node

print(lcm(*n_steps_))

