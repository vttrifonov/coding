# %%
def kmp(x, y):
    t = [-1]*(len(x)+1)
    p = 0
    for i in range(1, len(x)):
        if x[i]==x[p]:
            t[i] = t[p]
        else:
            t[i] = p
            while p>=0 and x[i]!=x[p]:
                p = t[p]
        p = p + 1
    t[-1] = p

    i, j, r = 0, 0, []
    while True:
        if j==len(x):
            r.append(i-j)
            j = t[j]
        elif i==len(y):
            break
        elif y[i]==x[j]:
            i = i + 1
            j = j + 1
        elif t[j]<0:
            i = i + 1
            j = 0
        else:
            j = t[j]

    return r

# %%
print(kmp('abac', 'caba'))

# %%
