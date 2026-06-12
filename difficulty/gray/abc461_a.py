import sys
input = sys.stdin.readline

def main():
    a,d = map(int,input().split())

    if a > d:
        print("No")
    else:
        print("Yes")
if __name__ == "__main__":
    main()