import test
import pprint
from tabulate import tabulate
import copy
pp = pprint.PrettyPrinter(indent=0)

def addOutline(table):
	n=len(table)
	m=len(table[0])
	for i,row in enumerate(table):
		table[i] = [i+1]+table[i]
	return table

rhotab = test.rho_table(10)
tautab = test.tau_table(10)
kaptab = test.table_fake(10)


tautab = addOutline(tautab)
kaptab = addOutline(kaptab)
rhotab = addOutline(rhotab)
# kaptab[0][0] = 'kappa(a,b)'
# rhotab[0][0] = 'rho(a,b)'
# tautab[0][0] = 'tau(a,b)'
print tabulate(rhotab,['rho(a,b)']+range(1,31),tablefmt="pipe")
print 
print tabulate(tautab,['tau(a,b)']+range(1,31),tablefmt="pipe")
print 
print tabulate(kaptab,['kappa(a,b)']+range(1,31),tablefmt="pipe")
