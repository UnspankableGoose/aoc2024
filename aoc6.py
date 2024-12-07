with open("data.txt", "r") as data:
    data = data.readlines()
    grid = {(y, x):data[y][x] for y in range(len(data)) for x in range(len(data[0]) - 1)}
    w = len(data[0]) - 1
    h = len(data)

def simulate(grid, oblock=None):
    grid = grid.copy()
    for y, x in grid:
        if grid.get((y, x), 0) == "^":
            pos = (y, x)
            
    if oblock:
        grid[oblock] = "#"
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    ans = 1
    facing = 0
    visited = set()
    while grid.get((pos[0], pos[1]), -1) != -1:
        nextpos = (pos[0] + delta[facing][0], pos[1] + delta[facing][1])
        while grid.get(nextpos, 0) == "#":
            facing = (facing + 1) % 4          
            nextpos = (pos[0] + delta[facing][0], pos[1] + delta[facing][1])
        pos = nextpos
        state = (facing, pos)
        if state not in visited:
            visited.add(state)
        else:
            return True
        if grid.get(pos, 0) == ".":
            grid[pos] = "X"
            ans += 1
    
    if oblock:
        return False

    return (grid, ans)

#part 1
print(simulate(grid)[1])
grid_1 = simulate(grid)[0].copy()

#part 2
ans = 0
for i in range(h):
    for j in range(w):
        if grid_1.get((i, j)) == "X":
            if simulate(grid, (i, j)) == True:
                ans += 1

print(ans)



