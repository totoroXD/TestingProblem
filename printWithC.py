import test
from tabulate import tabulate
def addOutline(table):
	n=len(table)
	m=len(table[0])
	for i,row in enumerate(table):
		table[i] = [i+1]+table[i]
	return table
n=10
m=35
tab=[x[:] for x in [[0]*m]*n]
for a in range(1,n+1):
	for b in range(1,m+1):
		if a<=b: tab[a-1][b-1]=a+b+1-len(test.find_real_fake_with_c(a,b))

tab = addOutline(tab)
print tabulate(tab,['tauc(a,b)']+range(1,m+1),tablefmt="pipe")
