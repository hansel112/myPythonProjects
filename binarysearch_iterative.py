# Iterative Binary Search Function method Python Implementation
# It returns index of n in given list if present,
# else returns -1
def binary_search(list, n):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        # for get integer result
        mid = (high + low) // 2

        # Check if n is present at mid
        if list[mid] < n:
            low = mid + 1

            # If n is greater, compare to the right of mid
        elif list[mid] > n:
            high = mid - 1

            # If n is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the list, return -1
    return -1


# Initial list
list = []
print('Enter the size of the list: ', end="")
size = int(input())

print('Enter ', size, 'values to search from:')
for i in range(size):
    list.append(input())

print('Enter the value to be searched: ', end="")
n = input()

# Function call
result = binary_search(list, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")