import logging
import sys

logger = logging.getLogger('simple_example')

N=13;

def subsums(nums):
    n=sum(nums)
    has=[True]+[False]*n
    for v in nums:
        for j in xrange(n-v,-1,-1):
            if has[j]: has[j+v]=True
    return has

def subsums_exclude(nums, exi):
    n=sum(nums)
    has=[True]+[False]*n
    for i in xrange(len(nums)):
        v=nums[i]
        if i==exi: continue
        for j in xrange(n-v,-1,-1):
            if has[j]: has[j+v]=True
    return has
def sumsofroot(n,chds):
    nums=[]
    for v in chds:
        nums.append(v[0])
    nums.append(n-1-sum(nums))
    return subsums(nums)
def merge_sums(hasa, hasb):# merge b into a
    for i in xrange(len(hasb)):
        hasa[i]=hasa[i]|hasb[i]
trees_a=[]
partitions_a=[]
def partitions(n):
    def dfs(n, nums, res):
        if n==0:
            res.append(nums[:])
            # print nums
        for v in xrange(1 if len(nums)==0 else nums[len(nums)-1], n+1):
            nums.append(v)
            dfs(n-v,nums,res)
            nums.pop()
    res=[];
    dfs(n,[],res)
    return res

def trees(n): #return [ tree, [(.,.), (.,.)...],...] tree:[(chdsize, chdid), (.,.), ...]
    def dfs_chd(n, parts, chds, now_chd, res):
        if now_chd>= len(parts): 
            res.append(chds[:])
            return
        # print n, parts, now_chd
        if 0<now_chd and parts[now_chd-1]==parts[now_chd]:
            chds.append(chds[len(chds)-1])
            dfs_chd(n, parts, chds, now_chd+1, res)
            chds.pop()
            return
        for v in xrange(len(trees_a[parts[now_chd]])):
            chds.append((parts[now_chd],v))
            dfs_chd(n, parts, chds, now_chd+1, res)
            chds.pop()
    if n==0: return [[]]
    if n==1: return [[(0,-1)]]
    res=[]
    chd=[]
    for partition in partitions_a[n-1]:
        dfs_chd(n, partition, chd, 0, res)
    return res
def go_tree(n, v, has):# now at node 
    if n==1:
        has[1]=has[n-2]=True
        return
    chds=trees_a[v[0]][v[1]];
    merge_sums(has,sumsofroot(n, chds))
    for u in chds:
        go_tree(n,u,has)
def set2int(sett):
    res=0
    for i in range(len(sett)):
        if sett[i]: res|=(1<<i)
    return res
def int2set(setb):
    res=[]
    for i in range(32):
        if setb&(1<<i): res.append(i)
    return res
for i in xrange(N+1):
    pts=partitions(i)
    partitions_a.append(pts[:])

Tavoid=[] #T[n][k]: exist size-n tree avoid k
Tssset=[] #T[n]: set of subset-sums for all size-n tree
Tid=[]
for i in xrange(N+1):
    Tavoid.append([False]*(N+1))
    Tid.append([0]*(N+1))
    Tssset.append({set2int([True]*(i))})
for i in xrange(N+1):
    ts=trees(i)
    trees_a.append(ts[:])
    for treeid in xrange(len(ts)):
        has=[True]+[False]*i
        go_tree(i,(i,treeid),has)
        Tssset[i].add(set2int(has))
        for j in range(i):
            if not has[j]:
                Tavoid[i][j]=True
                Tid[i][j]=treeid
                # print trees_a[i][treeid]
                # print has
    print '#tree',i,':',len(ts),'avoid',Tssset[i]
# for i in xrange(N+1):
def find_real_fake_with_c(a,b):# not cycle
    def dfs(n, nums,has,res):
        if len(nums)+n<=len(res):return
        if n==0:
            print nums
            ok=True
            tres=nums[:]
            for i in range(len(nums)):
                if not ok: break
                ss=subsums_exclude(nums,i)
                ss=ss[0:a+1]
                ss.reverse()
                ss=~set2int(ss)
                tok=False
                for t in Tssset[nums[i]]:
                    if (t|ss)==ss:# has 
                        tok=True
                        tres[i]=t
                        break
                if not tok: ok=False
            if ok:
                while len(res):res.pop()
                for i in range(len(nums)):
                    res.append((nums[i], tres[i]))
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
    has=[False]*(a+b+2)
    has[0]=True;
    dfs(a+b+1, nums, has, res)
    return res
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
