

ch_no = int(input("Enter a number of children : "))
pz_no = int(input("Enter a number of puzzles : "))
pzs = []
pz_sa = []
diffs = []
for i in range(pz_no):
    x = int(input("Enter the number of pieces in puzzle : "))
    pzs.append(x)

pzs.sort()
for i in range(pz_no-1):
    if len(pzs[i:i+ch_no]) < ch_no:
        break
    l = pzs[i:i+ch_no]
  
    
    diff = l[-1] - l[0]
    diffs.append(diff)
o = min(diffs)
print(o)