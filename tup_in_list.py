# given input
a = [12,34,56,78,90]
v = []

# require output
#[(12,34),(34,56),(56,78),(78,90)]


for i in range(len(a)-1):
    #k = tuple(a[i:i+2])
    #print(k)
    v.append(tuple(a[i:i+2]))
    
print(v)
