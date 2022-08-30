from collections import deque

q_1 = deque([])
q_1.append(1)   # [1]
q_1.append(2)   # [1, 2]
q_1.append(3)   # [1, 2, 3] - [2, 3] - [3] - []
print(q_1)
q_1.popleft()
print(q_1)
