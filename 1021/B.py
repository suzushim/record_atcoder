import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    num=0
    ninzu_list=[]
    time_list = []
    for i, v in enumerate(lines):
        if(i==0):
            num=int(v)
        else:
            ninzu, zikan = list(map(int, v.split()))
            ninzu_list.append(ninzu)
            time_list.append(zikan)
    
    def checker(now_time):
        sum_ninzu=0
        for i, t in enumerate(time_list):
            t_part = t+now_time
            if(t_part>=24):
                t_part-=24
            if(t_part>=9)and(t_part<=17):
                sum_ninzu+=ninzu_list[i]
        return sum_ninzu

    maxninzu=0
    for i in range(24):
        ninzu=checker(i)
        if(ninzu>=maxninzu):
            maxninzu=ninzu
    
    print(maxninzu)



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)