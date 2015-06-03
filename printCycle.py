import test
import pprint
from tabulate import tabulate

def addOutline(table):
	n=len(table)
	m=len(table[0])
	table = [range(0,m+1)]+table
	for i,row in enumerate(table):
		if i: table[i] = [i]+table[i]
	return table
cytab = test.cycle_table(10)
cytab = addOutline(cytab)
cytab[0][0]='a'
cytab[0][1]='b: rho(a,b) start to cycle by theorem'
cytab[0][2]='b: rho(a,b) start to cycle by computer comfirmation'
print tabulate(cytab,tablefmt="latex")