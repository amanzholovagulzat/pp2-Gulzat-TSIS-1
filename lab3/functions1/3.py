def solve(heads, legs):
    ifallchicken = heads * 2
    rabbits = (legs - ifallchicken)/2
    chicken = heads - rabbits
    return chicken, rabbits
numheads = 35
numlegs = 94
print(solve(35, 94))    