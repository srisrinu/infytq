from collections import namedtuple
n=int(input())
categories=input().split()
Student=namedtuple('Student',categories)
marks=[(Student._make(input().split()).NAME) for _ in range(n)]
print(*marks)