def time_to_seconds(time_str):
    mm, ss = map(int, time_str.split(':'))
    return mm * 60 + ss

def seconds_to_time(seconds):
    mm = seconds // 60
    ss = seconds % 60
    return f"{mm:02}:{ss:02}"

def solution(video_len, pos, op_start, op_end, commands):
    video_length = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    opening_start = time_to_seconds(op_start)
    opening_end = time_to_seconds(op_end)
    
    if opening_start <= current_pos <= opening_end:
        current_pos = opening_end
    
    for command in commands:
        if command == "prev":
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            current_pos = min(video_length, current_pos + 10)

        if opening_start <= current_pos <= opening_end:
            current_pos = opening_end
    
    return seconds_to_time(current_pos)