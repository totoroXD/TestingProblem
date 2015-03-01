import test
import pprint
from tabulate import tabulate

pp = pprint.PrettyPrinter(indent=0)
def addOutline(table):
	n=len(table)
	m=len(table[0])
	table = [range(0,m+1)]+table
	for i,row in enumerate(table):
		if i: table[i] = [i]+table[i]
	return table
tautab = rhotab = test.table(20)
rhotab = addOutline(rhotab)
rhotab[0][0] = 'rho(a,b)'
for i,row in enumerate(tautab):
	for j, ele in enumerate(row):
		a=i+1
		b=j+1
		tautab[i][j] = a+b-ele
tautab = addOutline(tautab)
tautab[0][0] = 'tau(a,b)'
print tabulate(rhotab,tablefmt="latex")
print tabulate(tautab,tablefmt="latex")