import sys
input = sys.stdin.readline

def main():
    count = 0
    n, m = map(int, input().split())

    while m != 0:
        m = n % m
        count += 1
    print(count)


if __name__ == "__main__":
    main()