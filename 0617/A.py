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
        if(i==0):
            num=int(v)
        else:
            s = list(str(v))
    
    s2=""
    for tango in s:
        s2+=tango*2
    
    print(s2)





if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)