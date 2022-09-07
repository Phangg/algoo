# 큐

N = 3
q = [0] * N
front = -1
rear = -1

rear += 1           # enqueue(10)
q[rear] = 10

rear += 1           # enqueue(20)
q[rear] = 20

rear += 1           # enqueue(30)
q[rear] = 30

front += 1          # dequeue()
print(q[front])

front += 1          # dequeue()
print(q[front])

front += 1          # dequeue()
print(q[front])

print()
#----------------------------------------------------------------------
# 원형 큐

N = 3
q = [0] * N
front = 0
rear = 0

rear = (rear+1) % N           # enqueue(10)
q[rear] = 10

rear = (rear+1) % N           # enqueue(20)
q[rear] = 20

rear = (rear+1) % N           # enqueue(30) / 원형 큐는 front 를 비워두고 사용하는 것이라, 사실 이미 큐를 덮어 쓰고 있는 중
q[rear] = 30                  # 큐의 크기가 꽉 차있을 때, 마지막 인덱스가 다시 앞으로 가는 순환이기 때문에, 덮어 쓰기 가능

rear = (rear+1) % N           # enqueue(40)
q[rear] = 40                  # 큐의 크기가 꽉 차있을 때, 마지막 인덱스가 다시 앞으로 가는 순환이기 때문에, 덮어 쓰기 가능

front = (front+1) % N         # dequeue()
print(q[front])

front = (front+1) % N         # dequeue()
print(q[front])

front = (front+1) % N         # dequeue()
print(q[front])

print()
#----------------------------------------------------------------------
# 같은 값이지만, 개수가 많아지면 느려짐
q = []

q.append(10)
q.append(20)
q.append(30)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print()
#----------------------------------------------------------------------
from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)
print(q.popleft())
print(q.popleft())
print(q.popleft())

print()
#----------------------------------------------------------------------

def BFS(G, v):                              # G: 그래프 / v: 탐색 시작점
    visited = [0] * (n+1)                   # n: 노드 개수
    queue = []                              # 큐 생성
    queue.append(v)                         # 시작점 큐에 삽입
    while queue:                            # 큐가 비어있지 않은 동안
        t = queue.pop(0)                    # 큐의 첫 원소 반환
        if not visited[t]:                  # 방문하지 않은 곳이라면
            visited[t] = True               # 방문 표시
            visit(t)                        # 노드 t 에서 할일
            for i in G[t]:                  # t와 연결된 모든 노드에 대해서
                if not visited[i]:          # 방문하지 않은 곳이라면
                    queue.append(i)         # 큐에 삽입


#----------------------------------------------------------------------

def BFS(G, v, n):                           # G: 그래프 / v: 탐색 시작점
    visited = [0] * (n+1)                   # n: 노드 개수
    queue = []                              # 큐 생성
    queue.append(v)                         # 시작점 큐에 삽입
    visited[v] = 1
    while queue:                            # 큐가 비어있지 않은 동안
        t = queue.pop(0)                    # 큐의 첫 원소 반환
        visit(t)                            # 노드 t 에서 할일
        for i in G[t]:                      # t와 연결된 모든 노드에 대해서
            if not visited[i]:              # 방문하지 않은 곳이라면
                queue.append(i)             # 큐에 삽입
                visited[i] = visited[n] + 1 # n 으로 부터 1 만큼

# swea1219 bfs.py 참고

#----------------------------------------------------------------------
