import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    num = int(input())

    keta1 = num%10
    keta2 = num//10
    if(keta1>=3)and(keta1<=7):
        keta1=5
    elif(keta1>7):
        keta2+=1
        keta1=0
    else:
        keta1=0
        
    print(keta1+keta2*10)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)