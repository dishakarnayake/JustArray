# Find min and max value in the list

#using sorting function
arr = [2,4,6,8,9,10,1]                 #Time complexity of O(n Log(n))
a = sorted(arr)                        #Space complexity of O(n)
min_ = a[0]
max_ = a[-1]
print(f"min value is {min_} and max values {max_}")





# using minimum and maximum function
arr = [2,4,6,8,9,10,1]                 #time complexity of O(1)
min_ = min(arr)
max_ = max(arr)
print(f"min value is {min_} and max values {max_}")




# using recursive function
def getMin(arr,n):                      # time complexity of O(n)
    if (n==1):                          # space complexity of O(n)
        return arr[0]
    else:
        return min(arr[n-1],getMin(arr,n-1))
    
def getMax(arr,n):
    if (n==1):
        return arr[0]
    else:
        return max(arr[n-1],getMax(arr,n-1))
arr = [2,4,6,8,9,10,1]
n = len(arr)
print(f"min value is {getMin(arr,n)} and max values {getMax(arr,n)}")