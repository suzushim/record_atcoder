import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.

    for i, v in enumerate(lines):
        ori_num = int(v)
    
    for i in range(1, 20):
        if(pow(i, i)==ori_num):
            print(i)
            break
        if(i==19):
            print(-1)



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)