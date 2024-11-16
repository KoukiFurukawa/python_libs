# 方針メモ
# ## 重要
# 最大でも 2N^2 回しか探索できない。
# 形のみ分かっており、それ以外は何もわからない
# 出力からあり得る油田の位置を計算し、算出する

# ・油田を graph で管理 ← あんまりやる意味なさそう
# ・ヒートマップを作成
# ・0 っぽい油田を探してそこを含むマス + ありそうなマスでコストを下げる
# ・x 個の集合でペアを作っておおよその数を予想できないか？

# ・ここにx個, ここにy個, ってことは、ここはz個だな、という推測をしたい
# ・形だけ
#
# ・あり得る地形を出来る限り列挙。つまりは答えとなりうる地形を列挙して保存する
# ・始点が 400通り のため、最悪計算量は 400^20 全探索で宇宙が終わってしまう
# ・当てはまる譜面を全部試す方法では到底間に合わない

# やること :
# ・eps から提出された x がどれくらいずれている可能性があるのかを確かめる
# ・油田の総量は入力からわかるため、予測した部分の油田量一致していなければやり直し
# ・0 の確率が100%である選び方を目指してみる 

# step1 :
# ・全部あるかどうかを確かめる
# ・油田の可能性のあるマスを全部掘る

# step2 :
# ・nマス選択し、n-1マス掘る。残り1マスが 0 かどうかは計算する.
# ・nマスの掘方はランダム
# 
# step3 :
# ・重複に選択し、おおよその位置を把握.
# ・この時値が期待値を上回る場合、ダブっていると考え、地形推論を行う


import sys
import random



def main():
    # 初期値 ---------------------------------------------------------------- #
    input = lambda: sys.stdin.readline().rstrip()
    line = input().split()
    N,M,eps = int(line[0]), int(line[1]), float(line[2]) # N*N = マスの数, M = 油田の数, eps = エラーパラメータ
    
    # 油田の情報を格納
    # idnex ごとに 油田の図を所持している。
    field = []
    
    # 埋蔵量を格納
    reserves = [[-1]*N for _ in range(N)]
    
    # 出力用
    ans = []
    
    # 油田入力 -------------------------------------------------------------- #
    for _ in range(M):
        d, *vals = map(int,input().split())
        ps = []
        for i in range(d):
            ps.append((vals[2*i], vals[2*i + 1]))
        field.append(ps)
        
    # dist = distributed(N,eps)
    # dist = dist if dist < 0 else -(dist)
    # dist -= 1
    
    # 1行ずつ n マス単位で情報確認 ------------------------------------------- #
    for i in range(N):
        data_set = []
        for j in range(N):
            data_set.append((i,j))
        
        output = create_output(data_set)
        print(f"q {N} {output}")
        sys.stdout.flush()
        
        response_cnt = int(input())
        true_cnt = max(guess_true_val(N, response_cnt, eps))
        
        cnt = 0
        
        count_list = [j for j in range(N)]
        while cnt < true_cnt and count_list:
            dig = random.choice(count_list)
            print(f"q 1 {i} {dig}")
            sys.stdout.flush()
            
            response = input()
            if response != "0":
                cnt += 1
                ans.append((i,dig))
            count_list.remove(dig)
            
    
    print("a {} {}".format(len(ans), ' '.join(map(lambda x: "{} {}".format(x[0], x[1]), ans))))
    sys.stdout.flush()
    
    resp = input()
    if  resp == "1":
        exit()


def create_output(ls):
    return ' '.join(map(lambda x: "{} {}".format(x[0], x[1]), ls))

def distributed(k, esp):
    """平均μを求める
    """
    res = k * esp * (1 - esp)
    return res


def guess_true_val(k, x, esp):
    """分散抜きの値を推測する
    ・分散の関係ない値を算出, 要は山のてっぺんを求める
    ・そこからどれだけ散らばっているかを計算.
    ・x と出力された時、実際の値としてあり得るものを算出する
    
    頂点を t としたとき、分散処理された値は、
    2 * eps * (t - x) + 処理前の値 となっている。
    """
    res = []
    # 山の頂点 => k//2
    # round(2 * esp * (k//2 - x) + C) = x な値を見つけたい.
    for i in range(x * 2 + 1):
        if round(2*esp*(k//2-x)+i) == x:
            res.append(i)
        
    return res

def HeatMap(N, field):
    """HeatMap
    各マスに何個油田があるのかをチェックする。 \n
    これが 0 ならば答えに含めない
    """
    heat_map = [[0]*N for _ in range(N)]
    for oil_map in field:
        for i,j in oil_map:
            heat_map[i][j] += 1
    
    return heat_map
        

main()