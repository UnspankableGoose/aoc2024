with open("data.txt", "r") as f:
    f = f.readlines()
    grid = {(y, x):f[y][x] for y in range(len(f)) for x in range(len(f[0]) - 1)}

#part 1

count = 0
for y, x in grid:
    for dy, dx in [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]:
        test = "".join(grid.get((y+dy*i, x+dx*i), "") for i in range(4))
        count += test == "XMAS"

print(count)

#part 2
count = 0
for y, x in grid:
    if grid[(y, x)] == "A":
        lr = grid.get((y-1, x-1), "") + grid.get((y+1, x+1), "")
        rl = grid.get((y-1, x+1), "") + grid.get((y+1, x-1), "")

        count += {lr, rl} <= {"MS", "SM"}

print(count)
    
