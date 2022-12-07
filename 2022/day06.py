with open('input_files/day06.dat', 'r') as input_file:
    input = input_file.read()

ans = -1

for i in range(4, len(input)):
    if len(set([input[j] for j in range(i, i+4)])) == 4:
        ans = i+4
        break
print(ans)

ans = -1

for i in range(14, len(input)):
    if len(set([input[j] for j in range(i, i+14)])) == 14:
        ans = i+14
        break
print(ans)