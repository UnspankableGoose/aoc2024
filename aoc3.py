import re

res = 0
with open("data.txt", "r") as data:
    content = data.read()

#part 1

rawnums = re.findall("mul\(([0-9]+,[0-9]+)\)", content)
for vals in rawnums:
    res += int(vals.split(",")[0]) * int((vals.split(",")[1]))

print(res)

#part 2
mul_starts = [m.start(0) for m in re.finditer("mul\(([0-9]+,[0-9]+)\)", content)]
do_starts_unf = [m.start(0) for m in re.finditer("do\(\)", content)]
dont_starts = [m.start(0) for m in re.finditer("don't\(\)", content)]

res = 0
do_starts = [0]
do_ptr = 0
for dont in dont_starts:
    if do_ptr == len(do_starts_unf): break
    if do_starts_unf[do_ptr] < dont:
        do_starts.append(do_starts_unf[do_ptr])
    while do_starts_unf[do_ptr] < dont:
        do_ptr+=1
        if do_ptr == len(do_starts_unf): break

dont_ptr = 0
for do in do_starts:
    for mul in mul_starts:
        if mul > do:
            mul_ptr = mul_starts.index(mul)
            break
        
    for dont in dont_starts:
        if dont > do:
            dont_ptr = dont_starts.index(dont)
            break
        
    while mul_starts[mul_ptr] < dont_starts[dont_ptr]:
        print(rawnums[mul_ptr])
        res += int(rawnums[mul_ptr].split(",")[0]) * int(rawnums[mul_ptr].split(",")[1])
        print(mul_ptr, dont_ptr)
        mul_ptr+=1
    
print(res)
