import sys
import re
input = sys.stdin.readline

def main():
    s = input().strip()
    answer = re.sub(r'\D', '', s)
    print(answer)

if __name__ == "__main__":
    main()