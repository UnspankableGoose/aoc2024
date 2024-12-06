rules = [[0] for i in range(100)]
requests = []

with open("data.txt", "r") as data:
    for line in data.readlines():
        if (line[2] == "|"):
            rules[int(line[3:5])].append(int(line[0:2]))
        else:
            requests.append(line.strip().split(","))

def good(request):
    valid = True
    for a in range(len(request)):
        for b in range(a+1, len(request)):
            if rules[int(request[a])].count(int(request[b])) > 0:
                valid = False

    return valid

#p1

valids = []
for request in requests:
    valids.append(good(request))

ans = 0
for i in range(len(requests)):
    if valids[i]:
        ans += int(requests[i][(len(requests[i]))//2])

print(ans)

#p2
ans = 0
for i in range(len(requests)):
    if not valids[i]:
        tempres = []
        for a in range(len(requests[i])):
            index = 0
            for b in range(len(tempres)):
                if rules[int(requests[i][a])].count(int(requests[i][b])) > 0:
                    index += 1
                    
            tempres.insert(index, int(requests[i][a]))
        ans += tempres[len(tempres)//2]

print(ans)
                
