import logging
# import numpy

logger = logging.getLogger('simple_example')

def count(a,b):
    if a>b: a,b = b,a
    def dfs(n, nums,has, res):
        # print n
        if len(nums)+n<len(res):return
        if n==0:
            # print nums
            logger.debug(nums, len(nums))
            if len(nums)>len(res):
                while len(res):res.pop()
                for m in nums: res.append(m)
        for v in range(1 if len(nums)==0 else nums[len(nums)-1], n+1):
            nhas=has[:]
            ok=True
            for i in range(b,-1,-1):
                if nhas[i]:
                    nhas[i+v]=True
                    if i==a or i==b:
                        ok = False
                        break
            if not ok: continue
            nums.append(v)
            dfs(n-v,nums,nhas,res)
            nums.pop()
    res=[]
    nums=[]
    has=[False]*(a+b+1)
    has[0]=True;    
    dfs(a+b, nums, has, res)
    return res
def table(size, xeven=False, yeven=False):
    table=[x[:] for x in [[0]*(size+1)]*(size+1)]
    for i in range(size+1):
        table[i][0] = table[0][i]=i;
    for a in range(1, size+1):
        if a%2==1 and xeven: continue
        for b in range(1,size+1):
            if b%2==1 and yeven: continue
            p=a+b-len(count(a,b))
            logger.debug( a,',',b,':',p)
            table[a][b]=p
    return table
def triangle_table(size, xeven=False, yeven=False):
    table=[x[:] for x in [[0]*(size+1)]*(size+1)]
    for i in range(size+1):
        table[i][0] = table[0][i]=i;
    for a in range(1, size+1):
        if a%2==1 and xeven: continue
        for b in range(1,size-a+2):
            if b%2==1 and yeven: continue
            p=a+b-len(count(a,b))
            logger.debug( a,',',b,':',p)
            table[a][b]=p
    return table
def input():
    print 'keyin: a b (0 0 for end)'
    while True:
        line = raw_input().split()
        a=int(line[0])
        b=int(line[1])
        res = count(a,b)
        print '============================='
        print 'Result:'
        print '\tneed ',a+b-len(res),' edges'
        print '\t',res
        print '============================='
