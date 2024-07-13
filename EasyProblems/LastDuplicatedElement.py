# Print last duplicated element in the list

def  duplicatedLastElement(arr,n):
    if (arr == None or  n <=0):
        return -1
    for i in range(n-1 , 0 , -1):
        if arr[i] == arr[i-1]:
            return arr[i]
    print("No duplicate element found")
    
arr = [2,4,4,8,9,10,10]
n = len(arr)
print(duplicatedLastElement(arr,n))

# time complexity is O(n)
# space complexity is O(1)