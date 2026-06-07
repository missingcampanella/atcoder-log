import sys
input = sys.stdin.readline

def main():
    n = int(input())

    answer = int((n+1)/2 *10000)
    print(answer)

if __name__ == "__main__":
    main()