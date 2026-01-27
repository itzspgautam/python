words = ["Abc", "Abcd", "Abc", "Anj", "ASBH", "AS", "kl", "ko"]
groups={}
for w in words:
    l = len(w)
    if l not in groups:
        groups[l]=[]
    groups[l].append(w)
    
print(groups)