import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    height=0
    width=0
    locs=[]
    for i, v in enumerate(lines):
        if(i==0):
            height, width=map(int,v.split())
        else:
            locs.append(list(v))

    H = int(height)
    W = int(width)
    #print(locs)


    # 上下左右方向を取得
    adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # i行目j列目の空マス(.)を調査
    for i in range(H):
        for j in range(W):
            count=0
            # 隣接区画のクッキー(#)数を調査
            for dx, dy in adjacents:
                if(locs[i][j]=="."):
                    nx, ny = i + dx, j + dy
                    if (0 <= nx < H) & (0 <= ny < W):
                        if locs[nx][ny] == "#":
                            count += 1
            if(count>=2):
                print(f"{i+1} {j+1}")
                break



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)