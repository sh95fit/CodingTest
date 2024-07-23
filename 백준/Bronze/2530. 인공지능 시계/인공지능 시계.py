def calculate_end_time(current_time, cooking_time):
    hours, minutes, seconds = current_time
    total_seconds = hours * 3600 + minutes * 60 + seconds + cooking_time
    
    end_hours = (total_seconds // 3600) % 24
    total_seconds %= 3600
    end_minutes = total_seconds // 60
    end_seconds = total_seconds % 60
    
    return end_hours, end_minutes, end_seconds

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    current_time = list(map(int, data[:3]))
    cooking_time = int(data[3])
    
    end_time = calculate_end_time(current_time, cooking_time)
    
    print(*end_time)

if __name__ == "__main__":
    main()
