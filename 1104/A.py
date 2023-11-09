import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.

    for i, v in enumerate(lines):
        if(i==1):
            strlist = str(v)
    
    for i in range(len(v)-1):
        if(v[i]=="a")and(v[i+1]=="b"):
            print("Yes")
            break
        elif(v[i]=="b")and(v[i+1]=="a"):
            print("Yes")
            break
        if(i==len(v)-2):
            print("No")



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)