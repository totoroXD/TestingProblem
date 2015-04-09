import logging
import sys

logger = logging.getLogger('simple_example')

def find_real_fake(a,b): #choose max d if tie
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

def find_fake(a,b):
    if a>b: a,b = b,a
    def check(nums):
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
                #(nums[0],nums[i]) = (nums[i],nums[0])
                return i
        return -1
    def dfs(n, nums, res):
        if len(nums)+n<max(len(res), a):return
        if n==0 and len(nums)>len(res):
            # print nums
            logger.debug(nums, len(nums))
            cc=check(nums)
            if cc!=-1:
                while len(res):res.pop()
                for m in nums: res.append(m)
                (res[0],res[cc]) = (res[cc],res[0])
        for v in range(1 if len(nums)==0 else nums[len(nums)-1], n+1):
            nums.append(v)
            dfs(n-v,nums,res)
            nums.pop()
    res=[]
    nums=[]
    dfs(a+b, nums, res)
    return res


def q(n, a, b): #a<=b<=b
    def dfs(n, nums,has, res):
        if len(nums)+n<len(res):return
        if n==0:
            # print nums
            logger.debug(nums, len(nums))
            
            if len(nums)>len(res) and has[b]:
                while len(res):res.pop()
                for m in nums: res.append(m)
        for v in range(1 if len(nums)==0 else nums[len(nums)-1], n+1):
            nhas=has[:]
            ok=True
            for i in range(b,-1,-1):
                if nhas[i]:
                    nhas[i+v]=True
                    if i==a:
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
    dfs(n, nums, has, res)
    return res

def rho_table(size):
    table=[x[:] for x in [[0]*size]*size]
    for a in range(1, size+1):
        for b in range(1,size+1):
            p=len(find_real_fake(a,b))
            logger.debug( a,',',b,':',p)
            table[a-1][b-1]=p
    return table
def tau_table(size):
    table=rho_table(size)
    for a in range(1, size+1):
        for b in range(1,size+1):
            table[a-1][b-1]=a+b-table[a-1][b-1]
    return table
def compare(ta, tb):
    size=len(ta)
    table=[x[:] for x in [[0]*size]*size]
    for i in range(0,size):
        for j in range(0,size):
            if ta[i][j]<tb[i][j]:
                table[i][j]=tb[i][j]-ta[i][j]
    return table
def table_fake(size):
    table=[x[:] for x in [[0]*size]*size]
    for a in range(1, size+1):
        for b in range(1,size+1):
            p=a+b-len(find_fake(a,b))
            logger.debug( a,',',b,':',p)
            table[a-1][b-1]=p if p<a+b else 74
    return table


def triangle_table(size):
    table=[x[:] for x in [[0]*size]*size]
    for a in range(1, size+1):
        for b in range(1,size-a+2):
            print >>sys.stderr, a, ',', b
            p=len(find_real_fake(a,b))
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
    res = find_real_fake(a,b)
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
