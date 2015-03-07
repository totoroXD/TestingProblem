import logging
import sys

logger = logging.getLogger('simple_example')

def count(a,b): #choose max d if tie
    if a>b: a,b = b,a
    d = min_nonfactor(a)
    def dfs(n, nums,has, res):
        if len(nums)+n<len(res):return
        if n==0:
            # print nums
            logger.debug(nums, len(nums))
            if len(nums)>len(res) or (len(nums)==len(res) and d_in_ar(d,nums)>d_in_ar(d,res)):
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
    table=[x[:] for x in [[0]*size]*size]
    for a in range(1, size+1):
        if a%2==1 and xeven: continue
        for b in range(1,size+1):
            if b%2==1 and yeven: continue
            p=len(count(a,b))
            logger.debug( a,',',b,':',p)
            table[a-1][b-1]=p
    return table

def triangle_table(size):
    table=[x[:] for x in [[0]*size]*size]
    for a in range(1, size+1):
        for b in range(1,size-a+2):
            print >>sys.stderr, a, ',', b
            p=len(count(a,b))
            logger.debug( a,',',b,':',p)
            table[a-1][b-1]=p
    return table
def min_nonfactor(n):
    for i in range(1,3*n):
        if n%i: return i
def d_in_ar(d, ar):
    cnt=0
    for e in ar:
        if e==d: cnt+=1
    return cnt
def in_cycle(a,b):
    res = count(a,b)
    d = min_nonfactor(a)
    return d_in_ar(d,res) >= a/d
def cycle_table(size):
    table=[]
    for a in range(1,1+size):
        d=min_nonfactor(a)
        cnt=0
        for b in range(1,a*a*a+2):
            print >>sys.stderr, a, ',', b
            if in_cycle(a,b): cnt+=1
            else: cnt=0
            if cnt>=d:
                table = table+[[1+d*(d+1)*(a-1)+(a-a%d),b-d+1]]
                break
    return table