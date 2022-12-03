priorities = "!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open('input_files/day03.dat', 'r') as input_file:
    input = input_file.read().split('\n')

# part 1

ans = 0
for line in input:
    half1 = line[:int(len(line)/2)]
    half2 = line[int(len(line)/2):]

    for i in half1:
        if i in half2:
            ans += int(priorities.index(i))
            break

print(ans)

# Part 2

ans = 0
for group in range(0, int(len(input)), 3):
    for i in input[group]:
        if i in input[group+1] and i in input[group+2]:
            ans += int(priorities.index(i))
            break

print(ans)
