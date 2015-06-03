def min_non_factor(n):
	for i in range(1,n):
		if n%i: return i
def dfs(a, d, nums, has,res):
    if has[a]: return
    if len(nums)>len(res):
        while len(res):res.pop()
        for m in nums: res.append(m)
    # ans = max(ans, len(nums))
    # print nums
    # print has
    for v in range(1 if not len(nums) else nums[len(nums)-1],d):
        nhas=has[:]
        for i in range(a, -1, -1):
            # print i,len(has) 
            if nhas[i]: nhas[i+v]=True
        nums.append(v)
        dfs(a, d, nums, nhas,res)
        nums.pop()

for n in range(3,211):
    has=[False]*(2*n+1)
    has[0]=True
    ans=0
    res=[]
    dfs(n,min_non_factor(n),[],has,res)
    has=[False]*(2*n+1)
    print 'n=',n,'d=',min_non_factor(n),len(res)
    if len(res)!=n-1:
        while True: print 'jizz'