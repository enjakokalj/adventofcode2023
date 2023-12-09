from collections import defaultdict

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

start_node = "AAA"
stop_node = "ZZZ"
n_steps = 0
goal_reached = False
while not goal_reached:
    for direction in instructions:
        n_steps += 1
        i = 0 if direction == "L" else 1
        next_node = dict_connections[start_node][i]
        if next_node == stop_node:
            print("n_steps",n_steps)
            goal_reached = True
            break
        else:
            start_node = next_node

