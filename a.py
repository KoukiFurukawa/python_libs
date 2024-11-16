from collections import defaultdict, deque

h,w = map(int,input().split())
a = [input().split() for _ in range(h)]
n = int(input())
alphabet = [chr(i) for i in range(97, 97+26)] # 小文字
graph = [[] for _ in range(26)]
depth = {}
eat_list = {}
depth_alp = defaultdict(list)

for i in range(n):
    n1,n2 = input().split()
    graph[alphabet.index(n1)].append(alphabet.index(n2))
    if n1 not in eat_list:
        eat_list[n1] = []
    if n2 not in eat_list:
        eat_list[n2] = []
    eat_list[n1].append(n2)

def dfs(n):
    global depth, graph
    stack = deque([n])
    if n not in depth:
        depth[n] = 0
    depth[n] = max(0, depth[n])
    while stack:
        x = stack.popleft()
        for i in graph[x]:
            if i not in depth:
                depth[i] = 0
            depth[i] = max(depth[x] + 1, depth[i])
            stack.append(i)

def solve(p):
    for i in range(h):
        for j in range(w):
            if a[i][j] == p:
                eat(i,j,p)
                
def eat(y,x, eater):
    # eater = string
    s = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    for addy,addx in s:
        nx, ny = addx + x, addy + y
        if 0 <= nx < w and 0 <= ny < h and a[ny][nx] in eat_list[eater]:
            a[ny][nx] = "-"
            
    
for i in range(26):
    if len(graph[i]) != 0:
        dfs(i)

# print(graph)
for i in depth:
    depth_alp[depth[i]].append(alphabet[i])
# print(depth_alp)



for i in depth_alp:
    for j in depth_alp[i]:
        solve(j)
        
for i in a:
    print(*i, sep=" ")