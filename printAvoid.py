import test
import pprint
# from tabulate import tabulate
import copy
# pp = pprint.PrettyPrinter(indent=0)

def addOutline(table):
	n=len(table)
	m=len(table[0])
	for i,row in enumerate(table):
		table[i] = [i+1]+table[i]
	return table

avdtab = test.Tavoid
print 

# avdtab = addOutline(avdtab)

# print tabulate(avdtab,['avoid(a,b)']+range(1,31),tablefmt="pipe")
# print 
# pprint.pprint(avdtab)
for i in xrange(len(avdtab)):
    for j in xrange(len(avdtab)):
        if avdtab[i][j]: print 1,
        else: print 0,
    print 