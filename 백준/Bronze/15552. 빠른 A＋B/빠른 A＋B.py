import sys

def sum_res():
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B)

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        sum_res()