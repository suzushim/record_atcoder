import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.


    for i, v in enumerate(lines):
        a,b = v.split()
    
    placedict={"A":0, "B":3, "C":4, "D":8, "E":9, "F":14, "G":23}

    place1 = placedict[a]
    place2 = placedict[b]

    print(abs(place1-place2))

    


    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)