from collections import deque

def bfs():
  global min_distance
  global cheack
  #방향벡터
  dx=[1,0,0]
  dy=[0,-1,0]
  dz=[0,0,1]
  while queue:
    x,y,z,n=queue.popleft()
    if x==X-1 and y==0 and z==Z-1:  #종점 도달
      if n in min_distance: min_distance[n]+=1  #이미 그 경로가 있으면 count
      else: min_distance[n]=1  #해당 경로가 처음이면 추가
    for i in range(3):  #방향_최단거리임을 고려하여
      nx=x+dx[i]
      ny=y+dy[i]
      nz=z+dz[i]
      if (z,y,x) in cheack:  #범위 내 끝지점에서 도달
        queue.append((nx,ny,nz,n+1)) #경우의 수가 나뉘기 때문에 단순히 n+=1하면 안됨
      if  nx<X and 0<=ny and nz<Z and graph[nz][ny][nx]==0:  #해당 값이 범위에 포함되는지 확인
        queue.append((nx,ny,nz,n+1))  #다음 스텝으로 이동
  return min_distance

if __name__=="__main__":
  Z,Y,X=map(int,input('범위 내에서 제외할 점을 선택하시오, 면 행 열순: ').split())  # ex) '5 5 2'you


  min_distance={}
  graph=[[[0]*X]*Y]*Z
  queue = deque()
  cheack=[(0,0,0), (Z-1,0,0), (Z-1,Y-1,0), (0,Y-1,0), (0,0,X-1), (Z-1,0,X-1), (0,Y-1,X-1), (Z-1,Y-1,X-1)]

  n=int(input('제외할 점의 개수를 입력하시오: '))
  for i in range(n):
    c,b,a=map(int,input('범위 내에서 제외할 점을 선택하시오, 면 행 열순: ').split())  # ex) '5 5 2'
    graph[c-1][b-1][a-1]=1
  queue.append((0,Y-1,0,0))
  print(bfs())