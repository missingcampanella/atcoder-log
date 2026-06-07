import sys
input = sys.stdin.readline

def main():
    s = input().strip()
    print(s+"pp")

if __name__ == "__main__":
    main()

# .strip()とは　空白や改行など目に見えないものを消すもの　基本は(s+"pp")でOK
# import sys
# input = sys.stdin.readline　の部分が勝手に改行してたっぽい？