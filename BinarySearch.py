arr = list(map(int, input("Enter the elements of the array: ").split()))
key = int(input("Enter the key to be searched: "))

low = 0
high = len(arr) - 1
found = False

while low <= high and not found:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("The key is present at position:", mid)
        found = True
    elif arr[mid] > key:
            high = mid - 1
    else:
            low = mid + 1

if not found:
    print("The key is not present in the array.")
