#YES,NOの大文字、小文字に注意

import sys
input = sys.stdin.readline

def main():
    n = int(input())

    if (n % 3) == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()