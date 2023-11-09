import sys

class Node:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"(row:{self.row}, col:{self.col}, arrival:{self.arrival})"

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.

    height=0
    width=0
    map_list=[]
    for i, v in enumerate(lines):
        if(i==0):
            height, width = list(map(int, v.split()))
        else:
            map_list.append(list(map(str, list(v))))

    # Nodeインスタンスを作成
    nodes = [[Node(i, j) for j in range(width)] for i in range(height)]

    stack=[]
    adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    counter=0

    # i行目j列目が#のとき　⇒　.に変換 + 隣接マスの#も.に変換
    for i in range(height):
        for j in range(width):
            if(map_list[i][j]=="#"):
                stack.append(nodes[i][j])
                while(stack):
                    node = stack.pop()
                    if(map_list[node.row][node.col]=="#"):
                        map_list[node.row][node.col]="."
                    for dx, dy in adjacents:
                        nx, ny = node.row + dx, node.col + dy
                        if (0 <= nx < height) and (0 <= ny < width):
                            if (map_list[nx][ny] == "#"):
                                stack.append(nodes[nx][ny])
                counter+=1
    
    print(counter)

    


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)