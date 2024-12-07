f = [l.strip() for l in open("input.txt")]

def gen(n,ops): # all op sequences of length n
  if n==1: return ops
  r = []
  for oo in gen(n-1,ops):
    for o in ops: r.append(oo+o)
  return r

def calculate(n,o):
  s = n[0]
  for i in range(len(o)):
    if o[i]=="+": s += n[i+1]
    elif o[i]=="*": s *= n[i+1]
    else: s = int(str(s)+str(n[i+1]))
  return s

def solve(l,ops):
  r,t = l.split(": "); r=int(r) # result to get
  n = tuple(map(int,t.split())) # numbers
  for o in gen(len(n)-1,ops):
    if calculate(n,o) == r: return r
  return 0

print(sum(solve(l,"+*") for l in f))
print(sum(solve(l,"+*&") for l in f))