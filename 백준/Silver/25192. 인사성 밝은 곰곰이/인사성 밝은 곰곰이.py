def count_gomgom_usage(records):
    count = 0
    users = set()
    
    for record in records:
        if record == "ENTER":
            users.clear()
        else:
            if record not in users:
                count += 1
                users.add(record)
    
    return count

n = int(input())
records = [input().strip() for _ in range(n)]

print(count_gomgom_usage(records))
