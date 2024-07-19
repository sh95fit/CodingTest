def time_to_seconds(time):
    h, m, s = map(int, time.split(':'))

    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60

    return f"{h:02}:{m:02}:{s:02}"

def calculate_remaining_time(current_time, start_time):
    current_seconds = time_to_seconds(current_time)
    start_seconds = time_to_seconds(start_time)

    if start_seconds <= current_seconds:
        start_seconds += 24 * 3600

    remaining_seconds = start_seconds - current_seconds

    return seconds_to_time(remaining_seconds)

current_time = input().strip()
start_time = input().strip()

remaining_time = calculate_remaining_time(current_time, start_time)
print(remaining_time)

