"""
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
"""


"""
getSimilarWords function use searchTerm to look through the english dictionary [from the wordList array].
"""
def getSimilarWords(searchTerm):
    wordList = []
    with open("./Online/dictionary.txt",'r') as f:
        wordList = f.read().split(",")
        f.close()
    resultArr = getClosestMatches(searchTerm,
          wordList, n=5, cutoff=0.75)
    return [text for text,score in resultArr]

"""
getClosestMatches is a function that will sort the results using quickSort Algorithm
and check if the similar score is above the threshold.
"""
def getClosestMatches(word, possibilities, n=3, cutoff=0.6):
    result = []
    for x in possibilities:
        score = jaro_Winkler(word,x)
        if score >= cutoff:
            result.append((x,score))
    quick_sort(result,0,len(result) - 1)
    return result[:-(n+1):-1]

"""
The Jaro-Winkler distance measures an edit distance between two sequences.
The higher the Jaro-Winkler distance, the more similar the string is.
"""
def jaro_Winkler(s1, s2) :
	jaro_dist = jaro_distance(s1, s2)
	# If the jaro Similarity is above a threshold
	if jaro_dist > 0.7:
		# Find the length of common prefix
		prefix = 0
		for i in range(min(len(s1), len(s2))) :
			# If the characters match
			if s1[i] == s2[i]:
				prefix += 1
			# Else break
			else :
				break

		# Maximum of 4 characters are allowed in prefix
		prefix = min(4, prefix)

		# Calculate jaro winkler Similarity
		jaro_dist += 0.1 * prefix * (1 - jaro_dist)

	return jaro_dist

"""
Jaro Distance use the position of the characters in the string 
and check if they are farther than the longer string's length divide 2 -1 characters apart.
If characters at the same position or shorter than the distance variable,
then it will increase the points. This score is the value m.
If no matching characters are found, it finds the number of transpositions.
A transposition is the number of matching characters that 
are not in the right order divide by two. This score is the value t.
To calculate the final value, 1/3(m/len(s1) + m/len(s2) + (m-t)/m)
"""
def jaro_distance(s1, s2) :
    # check if the string are the same
	if (s1 == s2) :
		return 1.0
	# get length of two strings
	len1 = len(s1)
	len2 = len(s2)

    # if string does not exist
	if (len1 == 0 or len2 == 0) :
		return 0.0

	# Maximum distance upto which matching is allowed
	max_dist = (max(len(s1), len(s2)) // 2 ) - 1

	# Count of matches
	match = 0

	# Hash for matches
	hash_s1 = [0] * len(s1) 
	hash_s2 = [0] * len(s2) 

	# Traverse through the first string
	for i in range(len1) :
		# Check if there is any matches
		for j in range( max(0, i - max_dist),
					min(len2, i + max_dist + 1)) :
			# If there is a match
			if (s1[i] == s2[j] and hash_s2[j] == 0) :
				hash_s1[i] = 1
				hash_s2[j] = 1
				match += 1
				break
	# If there is no match
	if (match == 0) :
		return 0.0

	# Number of transpositions
	t = 0

	point = 0

	# Count number of occurrences
	# where two characters match but
	# there is a third matched character
	# in between the indices
	for i in range(len1) :
		if (hash_s1[i]) :

			# Find the next matched character
			# in second string
			while (hash_s2[point] == 0) :
				point += 1

			if (s1[i] != s2[point]) :
				point += 1
				t += 1
			else :
				point += 1
				
		t /= 2

	# Return the Jaro Similarity Score
	return ((match / len1 + match / len2 +
			(match - t) / match ) / 3.0)

# Quick Sort Algorithm

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high][1] >= pivot[1]:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low][1] <= pivot[1]:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
