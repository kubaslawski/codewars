def sum_of_intervals(intervals):
    intervals.sort()

    intervals_sum = 0
    curr_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= curr_interval[1]:
           curr_interval = (curr_interval[0], max(curr_interval[1], intervals[i][1]))
        else:
            intervals_sum += curr_interval[1] - curr_interval[0]
            curr_interval = intervals[i]
    intervals_sum += curr_interval[1] - curr_interval[0]
    return intervals_sum









# x = sum_of_intervals([(1, 4), (3, 5), (7, 10)])
x = sum_of_intervals([(1, 5), (6, 10)])
print(x)