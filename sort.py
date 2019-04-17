def sortArrayDescending(newArray):
	SIZE = len(newArray)

	for i in range(SIZE):
		for j in range(SIZE-i-1):
			if (newArray[j]<newArray[j+1]):
				#Swap elements
				temp = newArray[j]
				newArray[j] = newArray[j+1]
				newArray[j+1] = temp
	return newArray
	#url_array = []

	#for pair_ in newArray:
	#	url_array.append(pair_[0])

	#return url_array