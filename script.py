import test
import pprint
# tab = test.table(22,0,0)
# fst=1
# for row in tab:
# 	print '|',
# 	for ele in row:
# 		if ele==0: print ' ',
# 		else: print ele,
# 		print '|',
# 	print ''
# 	if fst:
# 		fst=0
# 		for ele in row: print '|---',
# 		print '|'

# print '\n'
fst=1
tritab = test.triangle_table(60)
for row in tritab:
	print '|',
	for ele in row:
		if ele==0: print ' ',
		else: print ele,
		print '|',
	print ''
	if fst:
		fst=0
		for ele in row: print '|---',
		print '|'
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(tab)