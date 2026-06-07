import sys
input = sys.stdin.readline

def main():
    n = int(input())

    if (n % 2) == 0:
        print(n//2)
    else:
        print((n//2)+1)

if __name__ == "__main__":
    main()

# 2で割って切り上げるを式一つで表す方法
# (n + 1) // 2
# N=4（偶数）のとき: (4 + 1) // 2 = 5 // 2 = 2
# N=5（奇数）のとき: (5 + 1) // 2 = 6 // 2 = 3
# 0.5で切り捨てされていたのが1になって繰り上がる