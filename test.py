t=[9,127,130,62]
from itertools import combinations
print([" ".join(map(str, comb)) for comb in combinations(t,len(t)-1 )])
t2=[9,127,130]
x=[item for item in t if item not in t2]
print(x[0])