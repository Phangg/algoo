N = 9
arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]

# 최대 값
max_a = arr[0]  # 첫 원소를 최대 값으로 가정
for i in range(1, N):  # 나머지 모든 원소에 대해
    if arr[i] > max_a:
        max_a = arr[i]
print(max_a)
print()


# 최대 값의 인덱스
maxIdx = 0
for i in range(1, N):
    if arr[i] >= arr[maxIdx]:
        maxIdx = i
print(maxIdx)
print()

# 버블 소트
for i in range(N-1, 0, -1):  # 구간의 맨 끝 인덱스
    for j in range(i):  # 인접 원소 중 왼쪽 원소 인덱스
        if arr[j] > arr[j+1]:   # 더 큰 수를 오른쪽으로
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
print()

# 카운트 소트
tmp = [0] * N
c = [0] * (N+1)  # 0부터 N까지 숫자 개수, 인덱스가 N까지 있어야 함
for i in range(N):  # 카운트 배열
    c[arr[i]] += 1
for j in range(1, N+1):  # 개수 누적
    c[j] += c[j-1]
for i in range(N-1, -1, -1):  # 원본을 뒤에서부터 읽으면서 정렬 결과를 tmp 에 저장
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]
print(tmp)