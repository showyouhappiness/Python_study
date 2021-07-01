import collections

dq = collections.deque()

dq.append('c')
print(dq)
print(dq.pop())
print(dq)
print(dq.popleft())
print(dq)
dq.appendleft('d')
print(dq)
print(len(dq))
