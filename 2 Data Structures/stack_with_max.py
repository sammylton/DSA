import sys

stack = []
max_stack = []
outputs = []

q = int(sys.stdin.readline())
for _ in range(q):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        val = int(cmd[1])
        stack.append(val)
        max_stack.append(val if not max_stack else max(val, max_stack[-1]))

    elif cmd[0] == "pop":
        stack.pop()
        max_stack.pop()

    else:
        outputs.append(str(max_stack[-1]))

print("\n".join(outputs))
