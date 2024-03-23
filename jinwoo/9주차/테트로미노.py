tets = [
    [[0,0],[0,1],[0,2],[0,3]],
    [[0,0],[1,0],[2,0],[3,0]],
    
    [[0,0],[1,0],[0,1],[1,1]],

    [[0,0],[0,-1],[1,0],[2,0]],
    [[0,0],[0,1],[1,0],[2,0]],
    [[0,0],[2,-1],[1,0],[2,0]],
    [[0,0],[2,1],[1,0],[2,0]],
    [[0,0],[0,1],[0,2],[-1,0]],
    [[0,0],[0,1],[0,2],[-1,2]],
    [[0,0],[0,1],[0,2],[1,0]],
    [[0,0],[0,1],[0,2],[1,2]],
    
    [[0,0],[1,0],[1,1],[2,1]],
    [[0,0],[1,0],[1,-1],[2,-1]],
    [[0,0],[1,0],[0,1],[1,-1]],
    [[0,0],[0,1],[1,1],[1,2]],
    
    [[0,0],[-1,0],[1,0],[0,1]],
    [[0,0],[-1,0],[1,0],[0,-1]],
    [[0,0],[0,-1],[0,1],[-1,0]],
    [[0,0],[0,-1],[0,1],[1,0]],
]

N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

ans=0
for i in range(N):
    for j in range(M):
        for tet in tets:
            sum=0
            for dir in range(4):
                r = i + tet[dir][0]
                c = j + tet[dir][1]
                if r<0 or c<0 or r>=N or c>=M:
                    sum=-987654321
                    break
                sum+=arr[r][c]
            ans=max(ans,sum)     

print(ans)