import test
from tabulate import tabulate
def addOutline(table):
	n=len(table)
	m=len(table[0])
	for i,row in enumerate(table):
		table[i] = [i+1]+table[i]
	return table
n=13
m=40
tab=[x[:] for x in [[' ']*m]*n]
for a in range(1,n+1):
	for b in range(1,m+1):
		if a<=b: 
			r=a+b+1-len(test.find_real_fake_with_c(a,b))
			# if r<b+2:
			tab[a-1][b-1]=r

tab = addOutline(tab)
print tabulate(tab,['tauc(a,b)']+range(1,m+1),tablefmt="pipe")
for i in range(1,test.N+1):
	test.print_tree(i)