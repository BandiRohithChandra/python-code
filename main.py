def find_minimum_platforms(arr, dep):
   
    def time_to_minutes(t):
        hours, minutes = map(int, t.split(":"))
        return hours * 60 + minutes

    arr = [time_to_minutes(time) for time in arr]
    dep = [time_to_minutes(time) for time in dep]

    # Sort both arrays
    arr.sort()
    dep.sort()

    n = len(arr)
    platforms = 0  # Current platforms needed
    max_platforms = 0  # Maximum platforms needed
    i = j = 0  # Pointers for arrival and departure arrays

    while i < n and j < n:
        if arr[i] < dep[j]:
            # A train arrives
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            # A train departs
            platforms -= 1
            j += 1

    return max_platforms

# Example usage
arr = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

print("Minimum platforms required:", find_minimum_platforms(arr, dep))


