import sys
input = sys.stdin.readline

def main():
    s = "Helloworld"
    x =int(input())
    ans = s[:x] + s[x+1:]

    print(ans)
if __name__ == "__main__":
    main()