def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())

    num_operations = (n - 1) * n // 2

    degree = 2

    print(num_operations)
    print(degree)

if __name__ == "__main__":
    main()

