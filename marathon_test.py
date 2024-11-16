import sys
import random
import copy
from collections import (deque)
# メモ
# 方針1 ランダム　⇒ ほぼ最低点
# 方針2 貪欲方 ⇒ 再帰させて最低値が一番小さいところに選択する。
# 方針3 逆から解いてみる

def main():
    # 前準備 ##########################################
    input = lambda: sys.stdin.readline().rstrip()
    
    # 変数宣言 #######################################
    foods = list(map(int,input().split()))
    side_list = ["F","B","L","R"] #上下左右
    board = [0]*100
    output = ""
    
    for main_loop in range(100):
        
        place = int(input()) # どこに追加されたか
        
        #　お菓子追加 #######################################
        board = add_food(place, board, foods, main_loop)
        
        # 探索処理 ###########################################
        temporary_mini = {"F":[1000],"B":[1000],"L":[1000],"R":[1000]}
        for side in side_list:
            temporary_board = roll(side,board)
            for i in range(100-(main_loop+2)):
                new_list = temporary_board.copy()
                temporary_temporary_board = add_food(i+1,new_list,foods,main_loop+1)
                for side2 in side_list:
                    temporary_mini[side].append(DFS(roll(side2,temporary_temporary_board)))
        
            temporary_mini[side] = min(temporary_mini[side])
            
        # board = roll("F",board)
        
        # 出力準備 ##########################################
        res = {"side":[temporary_mini["F"],"F"]}
        for side in side_list:
            if res["side"][0] > temporary_mini[side]:
                res["side"][1] = side
                res["side"][0] = temporary_mini[side]
        
        output = res["side"][1]
        board = roll(output, board)
        
        # 出力 ###############################################
        print(output)
        sys.stdout.flush()


# お菓子を追加する。
def add_food(place, board, foods, main_loop) -> list:
    foods_cnt = 0
    for i in range(100):
        if board[i] == 0:
            foods_cnt += 1
            if foods_cnt == place:
                board[i] = foods[main_loop]
                return board
    print("バグっとるで")
    print(place,main_loop)
    print(*board,sep="\n")
    return 0

        
# 箱を傾けるとどうなるかなって関数
def roll(side,board) -> list:
    
    # 変数宣言 ###################################
    result = [[0]*10 for _ in range(10)]
    if side == "R":
        cnt_list = [0]*10
        for i in range(10):
            for j in range(10):
                j = (j+1)*-1
                if board[i][j] != 0:
                    result[i][-(cnt_list[i]+1)] = board[i][j]
                    cnt_list[i] += 1
    if side == "L":
        cnt_list = [0]*10
        for i in range(10):
            for j in range(10):
                if board[i][j] != 0:
                    result[i][cnt_list[i]] = board[i][j]
                    cnt_list[i] += 1
                    
    if side == "F":
        cnt_list = [0]*10
        for i in range(10):
            for j in range(10):
                if board[j][i] != 0:
                    result[cnt_list[i]][i] = board[j][i]
                    cnt_list[i] += 1
                    
    if side == "B":
        cnt_list = [0]*10
        for i in range(10):
            for j in range(10):
                j = (j+1)*-1
                if board[j][i] != 0:
                    result[-(cnt_list[i]+1)][i] = board[j][i]
                    cnt_list[i] += 1
                    
    # print(*result, sep="\n")
                            
    return result


# 連結成分の数を調べる関数
def DFS(board_set) -> int:
    
    # 変数宣言 ###############################
    visited = [[False]*10 for _ in range(10)]
    board = [[0]*10 for _ in range(10)]
    for i in range(100):
        board[i//10][i%10] = board_set[i]
    cnt = 0
    for i in range(10):
        for j in range(10):
            # DFSする
            if visited[i][j] != True and board[i][j] != 0:
                stack = deque([[i,j]])
                food = board[i][j]
                while stack:
                    x,y = stack.popleft()
                    visited[x][y] = True
                    for addX,addY in [[0,1],[0,-1],[1,0],[-1,0]]:
                        nx,ny = x+addX,y+addY
                        if 0 <= nx < 10 and 0 <= ny < 10 and visited[nx][ny] == False and board[nx][ny] == food:
                            stack.append([nx,ny])
                cnt += 1
    
    return cnt
    
if __name__ == "__main__":
    main()