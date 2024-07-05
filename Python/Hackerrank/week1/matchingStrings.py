#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

def matchingStrings(strings, queries):
    # Create a dictionary to store the frequency of each word
    frequency = {}
    for s in strings:
        frequency[s] = frequency.get(s, 0) + 1
    
    # Initialize a list to store the count of each query
    counts = []
    for q in queries:
        counts.append(frequency.get(q, 0))
    
    return counts

list1 = ['abc', 'def', 'ghi', 'abc']
list2 = ['def', 'xyz', 'abc']
res = matchingStrings(list1, list2)
print("Matching strings:", res)

