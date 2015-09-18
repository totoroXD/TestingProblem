import test
from tabulate import tabulate

tab=[x[:] for x in [[0]*16]*15]
for a in range(1,11):
	for b in range(1,16):
		if a<=b: tab[a-1][b-1]=a+b+1-len(test.find_real_fake_with_c(a,b))
	print

print tabulate(tab,tablefmt="pipe")