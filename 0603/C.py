import sys
import numpy as np
from collections import deque
def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    def dist(a1, a2):
        dis = pow(pow(a1[0]-a2[0], 2) + pow(a1[1]-a2[1], 2), 1/2)
        return dis
    distance=0
    num=0
    zahyo_list=[]
    for i, v in enumerate(lines):
        if(i==0):
            num, distance=list(map(int, v.split()))
        else:
            zahyo_list.append(list(map(int, v.split())))

    infection_list = [0]*num
    infection_list[0] = 1
    

    queue = deque([[0]])

    while queue:
        infected = queue.popleft()[0]
        #print(infected)

        for person in range(num):
            if(infection_list[person]==1):
                continue
            #print(dist(zahyo_list[infected],zahyo_list[person]))
            if(dist(zahyo_list[infected],zahyo_list[person]) <= distance):
                queue.append([person])
                infection_list[person]=1
        if(infection_list==[1]*num):
            break
    
    for i in range(num):
        if(infection_list[i]==1):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)