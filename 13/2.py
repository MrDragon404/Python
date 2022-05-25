stations1 = [0, 300, 375, 750, 950]
stations2 = [0, 200, 410, 670, 1200]
fuel = 400

def minStops(arr):
    res = 0
    start = 0
    stop = 1
    if arr[stop] - arr[start] > fuel:
        return 0

    while start < stop and stop < len(arr):

        if arr[stop] - arr[start] <= fuel:
            stop = stop + 1
        else:
            start = stop - 1
            res = res + 1
    return res

print(minStops(stations1))
print(minStops(stations2))
