import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    num=0
    s = []
    for i, v in enumerate(lines):
        nums = list(map(int, v.split()))

    s=0
    for i, num in enumerate(nums):
        s+=pow(2,i)*num
    
    print(s)





if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)