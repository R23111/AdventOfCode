with open('input_files/day02.dat', 'r') as input_file:
    input = input_file.read().split('\n')

# PART 1

points = {"X": 1, "Y": 2, "Z": 3}

total_points = 0

for i in input:
    total_points += points[i[2]]

    if i[2] == "X":
        if i[0] == "A":
            total_points += 3
        elif i[0] == "C":
            total_points += 6
    elif i[2] == "Y":
        if i[0] == "B":
            total_points += 3
        elif i[0] == "A":
            total_points += 6
    elif i[2] == "Z":
        if i[0] == "C":
            total_points += 3
        elif i[0] == "B":
            total_points += 6

print(total_points)

# PART 2

points = {"X": 0, "Y": 3, "Z": 6}

total_points = 0

for i in input:
    total_points += points[i[2]]

    if i[2] == "X":
        if i[0] == "A":
            total_points += 3
        elif i[0] == "B":
            total_points += 1
        elif i[0] == "C":
            total_points += 2

    elif i[2] == "Y":
        if i[0] == "A":
            total_points += 1
        elif i[0] == "B":
            total_points += 2
        elif i[0] == "C":
            total_points += 3

    elif i[2] == "Z":
        if i[0] == "A":
            total_points += 2
        elif i[0] == "B":
            total_points += 3
        elif i[0] == "C":
            total_points += 1

print(total_points)
