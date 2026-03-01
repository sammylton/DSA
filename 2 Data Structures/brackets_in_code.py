import sys

def check_brackets(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for i, ch in enumerate(text):
        if ch in "([{":
            stack.append((ch, i))
        elif ch in ")]}":
            if not stack or stack[-1][0] != pairs[ch]:
                return i + 1
            stack.pop()

    if stack:
        return stack[0][1] + 1

    return "Success"

if __name__ == "__main__":
    text = input().strip()
    print(check_brackets(text))
