def main():
	#content = raw_input()
	#test =  content.split('\n')
	#test = [2,-2,6,-6,8]
	s = 0
	sumList = []
	for a in test:
		s+=a
		sumList.append(s)
	sortedSumList = dict((i,sorted(sumList).count(i)) for i in sorted(sumList))
	sequences = 0
	for key,value in sortedSumList.iteritems():
		print key, value
		#if key = 0:
		if value > 1:
			sequences+= value*2-1
	print sequences
if __name__ == "__main__":
	main()