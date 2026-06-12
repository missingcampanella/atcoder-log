import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = "Yes"
    
    for i in range(n):
        if i + 1 != b[a[i]-1]:
            # i + 1 は「木こりの番号」、b[a[i]-1] は女神側の照合
            answer = "No"
            break
    print(answer)

if __name__ == "__main__":
    main()