import sys

# TLEにつき未完成
def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    num = 0
    start_list=[]
    end_list=[]
    for i, v in enumerate(lines):
        if(i==0):
            num = int(v)
        else:
            start, end = list(map(int, v.split()))
            start_list.append(start)
            end_list.append(end+start)

    comp_list=[0]*len(start_list)
    finaltime=max(end_list)
    counter=0
    for time in range(finaltime):
        time+=1
        maxend=finaltime
        prod=-1
        for i, end in enumerate(end_list):
            if(time>=start_list[i])and(time<=end):
                if(end<=maxend)and(comp_list[i]==0):
                    maxend=end
                    prod=i
        if(prod!=-1):
          counter+=1
          comp_list[prod]=1
    
    print(counter)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)