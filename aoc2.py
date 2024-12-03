reports = []

with open("data.txt", "r") as file:
    for line in file:
        reports.append(line.strip().split(" "))

for i in range(len(reports)):
    for j in range(len(reports[i])):
        reports[i][j] = int(reports[i][j])

unsafe_levels = 0
for level in reports:
    if sorted(level) != level and sorted(level, reverse = True) != level:
        unsafe_levels += 1
    else:
        for value in range(1, len(level)):
            diff = abs(level[value] - level[value-1])
            if (diff > 3 or diff < 1):
                unsafe_levels += 1
                break
            
print(len(reports) - unsafe_levels)

def safe(level, index):
    temp = level.copy()
    temp.pop(index)
    if sorted(temp) != temp and sorted(temp, reverse = True) != temp:
        return False
    else:
        for value in range(1, len(temp)):
            diff = abs(temp[value] - temp[value-1])
            if (diff > 3 or diff < 1):
                return False

    return True
    

safe_levels = 0
for level in reports:
    for rem in range(len(level)):
        if safe(level, rem):
            safe_levels+=1
            break

print(safe_levels)
