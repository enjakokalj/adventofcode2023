from collections import defaultdict

f = open("day05_input.txt", "r")
seeds = []

seed_to_soil2 = []
soil_to_fertilizer2 = []
fertilizer_to_water2 = []
water_to_light2 = []
light_to_temperature2 = []
temperature_to_humidity2 = []
humidity_to_location2 = []

info = -1
for line in f:
    #print(line)
    if line != "\n":
        line = line.strip().split(":")
        if line[0] == "seeds":
            seeds += [int(x) for x in line[-1].strip().split(" ")]
        elif line[0] == "seed-to-soil map":
            #destination range start, the source range start, and the range length
            info = 1
        elif line[0] == "soil-to-fertilizer map":
            #destination range start, the source range start, and the range length
            info = 2
        elif line[0] == "fertilizer-to-water map":
            #destination range start, the source range start, and the range length
            info = 3
        elif line[0] == "water-to-light map":
            #destination range start, the source range start, and the range length
            info = 4
        elif line[0] == "light-to-temperature map":
            #destination range start, the source range start, and the range length
            info = 5
        elif line[0] == "temperature-to-humidity map":
            #destination range start, the source range start, and the range length
            info = 6
        elif line[0] == "humidity-to-location map":
            #destination range start, the source range start, and the range length
            info = 7
        elif info == 1:
            line = [int(x) for x in line[0].split(" ")]
            destination = line[0]
            source = line[1]
            seed_to_soil2.append([line[1],line[0],line[-1]])
        elif info == 2:
            line = [int(x) for x in line[0].split(" ")]
            destination = line[0]
            source = line[1]
            soil_to_fertilizer2.append([line[1],line[0],line[-1]])
        elif info == 3:
            line = [int(x) for x in line[0].split(" ")]
            destination = line[0]
            source = line[1]
            fertilizer_to_water2.append([line[1],line[0],line[-1]])
        elif info == 4:
            line = [int(x) for x in line[0].split(" ")]
            destination = line[0]
            source = line[1]
            water_to_light2.append([line[1],line[0],line[-1]])
        elif info == 5:
            line = [int(x) for x in line[0].split(" ")]
            destination = line[0]
            source = line[1]
            light_to_temperature2.append([line[1],line[0],line[-1]])
        elif info == 6:
            line = [int(x) for x in line[0].split(" ")]
            destination = line[0]
            source = line[1]
            temperature_to_humidity2.append([line[1],line[0],line[-1]])
        elif info == 7:
            line = [int(x) for x in line[0].split(" ")]
            destination = line[0]
            source = line[1]
            humidity_to_location2.append([line[1],line[0],line[-1]])


#the closest location that needs a seed
#the lowest location number that corresponds to any of the initial seeds
print(seeds)
locations = []
for seed in seeds:
    #get soil
    for x in seed_to_soil2:
        if x[0] <= seed < x[0] + x[-1]:
            soil = seed + (x[1] - x[0])
            break
    else:
        soil = seed
    #get fertilizer
    for x in soil_to_fertilizer2:
        if x[0] <= soil < x[0] + x[-1]:
            fertilizer = soil + (x[1] - x[0])
            break
    else:
        fertilizer = soil
    # get water
    for x in fertilizer_to_water2:
        if x[0] <= fertilizer < x[0] + x[-1]:
            water = fertilizer + (x[1] - x[0])
            break
    else:
        water = fertilizer
    #get light
    for x in water_to_light2:
        if x[0] <= water < x[0] + x[-1]:
            light = water + (x[1] - x[0])
            break
    else:
        light = water
    #get temperature
    for x in light_to_temperature2:
        if x[0] <= light < x[0] + x[-1]:
            temperature = light + (x[1] - x[0])
            break
    else:
        temperature = light
    #get humidity
    for x in temperature_to_humidity2:
        if x[0] <= temperature < x[0] + x[-1]:
            humidity = temperature + (x[1] - x[0])
            break
    else:
        humidity = temperature
    #get location
    for x in humidity_to_location2:
        if x[0] <= humidity < x[0] + x[-1]:
            location = humidity + (x[1] - x[0])
            break
    else:
        location = humidity
    locations.append(location)
    print(seed,soil,fertilizer,water,light,temperature,humidity,location)
print(min(locations))

