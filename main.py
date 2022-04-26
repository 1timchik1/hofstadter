def male(n):
    if n == 0:
        return 0
    else:
        return n - female(male(n-1))

def female(n):
    if n == 0:
        return 1
    else:
        return n - male(female(n-1))
    
n = int(input())
F = []
M = []
for i in range(n + 1):
    F.append(female(i))
    M.append(male(i))
print("FEMALE:", *F)
print("MALE:", *M)
