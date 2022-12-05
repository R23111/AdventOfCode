# STRING MANIPULATIONS

with open('input_files/day05_1.dat', 'r') as input_file:
    input1 = input_file.read().split('\n')

with open('input_files/day05_2.dat', 'r') as input_file:
    input2 = input_file.read().split('\n')

stack = ["", "", "", "", "", "", "", "", ""]
instructions = []

for s in input1:
    for i in range(len(s)):
        stack[i] += s[i]
stack = [s.replace(" ", "") for s in stack]

for i in input2:
    temp = ""
    for c in i:
        if c.isnumeric() or c == " ":
            temp += c
    temp = temp[1:]
    temp = temp.split("  ")
    temp = [int(t) for t in temp]

    instructions.append(temp)

# PART 1

crates = stack.copy()

for ins in instructions:
    crates[ins[2]-1] = crates[ins[1]-1][:ins[0]][::-1] + crates[ins[2]-1]
    crates[ins[1]-1] = crates[ins[1]-1][ins[0]:]

ans = ""
for s in crates:
    if s != "":
        ans += s[0]
print(ans)

# PART 2
crates = stack.copy()
for ins in instructions:
    crates[ins[2]-1] = crates[ins[1]-1][:ins[0]] + crates[ins[2]-1]
    crates[ins[1]-1] = crates[ins[1]-1][ins[0]:]

ans = ""
for s in crates:
    if s != "":
        ans += s[0]
print(ans)
