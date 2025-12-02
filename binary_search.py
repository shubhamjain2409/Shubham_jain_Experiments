def binary_search(arr,target):

    l = 0
    n = len(arr)
    r = n - 1

    while(l<=r):
        mid = l + (r-l)//2

        if(arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            l = mid + 1

        else:
            r = mid - 1

    return -1


# This is a function for binary search.