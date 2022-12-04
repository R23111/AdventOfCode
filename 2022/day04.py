with open('input_files/day04.dat', 'r') as input_file:
    input = input_file.read().split('\n')

pairs = [i.split(',') for i in input]
pairs = [[p[0].split('-'), p[1].split('-')] for p in pairs]

ans = 0

for p in pairs:
    if (int(p[0][0]) >= int(p[1][0]) and int(p[0][1]) <= int(p[1][1])):
        ans += 1
    elif (int(p[1][0]) >= int(p[0][0]) and int(p[1][1]) <= int(p[0][1])):
        ans += 1
print(ans)


ans = 0

for p in pairs:
    for i in range(int(p[0][0]), int(p[0][1])+1):
        if i in [j for j in range(int(p[1][0]), int(p[1][1])+1)]:
            ans += 1
            break
print(ans)
