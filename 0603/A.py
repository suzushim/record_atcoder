import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    name_list = []
    age_list = []
    for i, v in enumerate(lines):
        if(i==0):
            continue
        else:
            a,b = v.split()
            name_list.append(a)
            age_list.append(int(b))

    rename_list = []
    minage=0
    min_index=0

    for i in range(len(age_list)):
        if(i==0):
            minage=age_list[i]
        if(age_list[i]<minage):
            minage=age_list[i]
            min_index=i
    
    for i in range(len(age_list)):
        index=min_index+i
        if(index>=len(age_list)):
            index-=len(age_list)
        rename_list.append(name_list[index])
    
    for i in rename_list:
        print(i)
    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
