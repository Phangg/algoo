import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
house = sorted(list(map(int, sys.stdin.readline().split())))

print(house[((n-1)//2)])