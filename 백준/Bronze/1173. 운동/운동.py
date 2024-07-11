def min_time_to_exercise(N, m, M, T, R):
    if m + T > M:
        return -1  

    current_time = 0
    exercise_time = 0
    current_pulse = m

    while exercise_time < N:
        if current_pulse + T <= M:
            current_pulse += T
            exercise_time += 1

        else:
            current_pulse -= R

            if current_pulse < m:
                current_pulse = m

        current_time += 1

    return current_time

N, m, M, T, R = map(int, input().split())

print(min_time_to_exercise(N, m, M, T, R))

