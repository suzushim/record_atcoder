import sys
import numpy as np

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.

    mass_map = []

    for i, v in enumerate(lines):
        mass_map.append(list(map(int, v.split())))
    
    # 重複あればFalse
    def checker(seq=[]):
        return len(seq) == len(set(seq))

    flag = True


    for ori_seq in mass_map:
        if(checker(ori_seq)==False):
            flag=False
    
    mass_map_T = np.array(mass_map).T
    for ori_seq in mass_map_T:
        if(checker(ori_seq)==False):
            flag=False
    
    mass_map_nine = [[] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if(i<=2):
                if(j<=2):
                    mass_map_nine[0].append(mass_map[i][j])
                elif(j<=5):
                    mass_map_nine[1].append(mass_map[i][j])
                else:
                    mass_map_nine[2].append(mass_map[i][j])
            elif(i<=5):
                if(j<=2):
                    mass_map_nine[3].append(mass_map[i][j])
                elif(j<=5):
                    mass_map_nine[4].append(mass_map[i][j])
                else:
                    mass_map_nine[5].append(mass_map[i][j])
            else:
                if(j<=2):
                    mass_map_nine[6].append(mass_map[i][j])
                elif(j<=5):
                    mass_map_nine[7].append(mass_map[i][j])
                else:
                    mass_map_nine[8].append(mass_map[i][j])
    

    for ori_seq in mass_map_nine:
        if(checker(ori_seq)==False):
            flag=False
    
    if(flag==True):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)