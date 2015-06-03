from test import *
def check(nums,a,b):
    # print nums
    for i in range(0,len(nums)):
        v=nums[i]
        has=[True]+[False]*(a+b)
        for j in range(0,len(nums)):
            if i==j: continue
            u=nums[j]
            for k in range(a+b-u,-1,-1):
                if has[k]: has[k+u]=True
        # print nums,v,has[b], has[a], has
        if has[b] and not has[a] and v<=a: 
            return v
    return -1
(a,b)=(8,20)
ar = find_real_fake(a,b-1)
print ar
af = find_fake(a,b)
print af,'\n',check(af,a,b)

ss = subsums(ar)
for i in range(0,len(ss)):
     print i,':',ss[i]