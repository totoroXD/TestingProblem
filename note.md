問題轉成圖論 子圖問題(problem.tex)

tau(a,b,0)>=floor(a+b,2)

c=0
- thereom: 轉化成 integer partition
- b夠大以d循環 d是a的最小非因數.   
 -b>=a*d (a=6不對)
 -b>=d(d+1)aH(p) (proved in cycle.tex)
 -應改有更小的b
- conject: tau(a,a~2a)=2a (a is even)
- exist tau(a,b-1) include b?
- conject: min{Q(a+b-i,a,b)|i=1~a-1}=Q(a+b-1,a,b)
c=1
- fact: 有比b+2更好的解

c>=2
- 重複用度數刪掉中性
- 一個環利用a,b特性

Outline
-
1. introduction
2. An Equivalence Graph Problem
 - (a+b)/2 lower-bound
3. Integer Partition
 - Thm (2,b)
 - Optimal solution via integer partitioning in O(a*2^sqrt(a+b))
4. Further Speedup
 - cycle proof
 - O(a*2^sqrt(d(d+1)a))
5. Open Problems
 - cycle 可以更早嗎？
 - Avoidance integer partitioning?

2/25
def of tau
close form
lemma 4.2
	不用bitset
thereom 4.3
	補 a/d
	
