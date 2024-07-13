# Find most frequent element in the list
# running two loops
def mostFrequentElement(arr,n):
    if (arr == None or  n <=0):
        return -1

    max_count = 0
    element_having_max_count = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > max_count:
            max_count = count
            element_having_max_count = arr[i]

    return element_having_max_count

arr = [2,4,4,8,9,10,10,10]
n = len(arr)
print(mostFrequentElement(arr,n))
# time complexity is O(n^2)
# space complexity is O(1)




# using Sorting
def MostFrequentElement(arr1,n1):
    arr1.sort()
    Max_count = 1
    res_ = arr1[0]
    Curr_count = 1
    for i in range(1,n1):
        if (arr1[i] == arr1[i-1]):
            Curr_count +=1
        else:
            Curr_count = 1
            
        if (Curr_count > Max_count):
            Max_count = Curr_count
            res_ = arr1[i]
    return res_

arr1 = [2,4,4,8,9,2,67,2,2]
n1 = len(arr1)
print(MostFrequentElement(arr1,n1))
# time complexity is O(n Log(n))
# space complexity is O(1)



#using hashing

def most_Frequent_Element(arr2,n2):
    d = {}
    for i in range(n2):
        if arr[i] in d:
            d[arr2[i]] += 1
        else:
            d[arr2[i]] = 1
    max_count = 0
    element_having_max_count = 0
    for i in d:
        if d[i] > max_count:
            max_count = d[i]
            element_having_max_count = i
    return element_having_max_count

arr2 = [2,4,4,8,9,10,10,10]
n2 = len(arr2)
print(most_Frequent_Element(arr2,n2))
# time complexity is O(n)
# space complexity is O(n)