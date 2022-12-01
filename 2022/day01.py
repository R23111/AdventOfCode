with open('input_files/day01.dat', 'r') as input_file:
    input = input_file.read().split('\n\n')

input = [map(int, i.splitlines()) for i in input]

# Part 1

sums = [sum(i) for i in input]
sums.sort()
print(sums[-1])

# Part 2

print(sum(sums[-3:]))
