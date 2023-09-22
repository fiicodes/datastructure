def maxMeetings(N, start, end):
    # Create a list of meetings with their start time, end time, and index
    meetings = [(start[i], end[i], i) for i in range(N)]

    # Sort meetings by end time
    meetings.sort(key=lambda x: x[1])

    # Initialize variables
    max_meetings = 0
    current_end_time = (
        -1
    )  # Initialize with a value that ensures the first meeting can be scheduled

    # Iterate through meetings
    for meeting in meetings:
        start_time, end_time, index = meeting

        # Check if the current meeting can be scheduled
        if start_time >= current_end_time:
            max_meetings += 1
            current_end_time = end_time

    return max_meetings


# Example usage:
N = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print(maxMeetings(N, start, end))  # Output: 4
