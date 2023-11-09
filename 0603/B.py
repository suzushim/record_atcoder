import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    num=0
    for i, v in enumerate(lines):
        num=int(v)
    keta = 0
    for i in range(6):
        if(num>pow(10,8-i)):
            keta+=1
            num //= 10
    print(num*pow(10, keta))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)