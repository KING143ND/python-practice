#=============== Q:18-Python Program for array rotation =================


def RotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print(f"Array after left rotation is: {RotateArray(arr, len(arr), 7)}")