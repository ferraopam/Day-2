inp = "Comprehensions are a feature of Python which I would miss if I ever have it.Comprehensions are constructs that allow sequences to be built from other sequences.Several types of comprehesions are supported in  both Python2 and Python3"
li = inp.strip(" ").split(" ")
di = {}
for l in li:
    if not l in di:
        di[l] = 1 
    else:
        di[l] += 1
ma = max(di.values())
mi = min(di.values())
for m,n in di.items():
    if n == ma or n == mi:
        print(f" {m} : {n}")