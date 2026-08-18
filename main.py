import sys

from trie import Trie

root = Trie()
size_count = 0
out = []

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line: continue
    parts = line.split(" ", 1)
    cmd = parts[0]; arg = parts[1] if len(parts) > 1 else ""
    if cmd == "INSERT":
        root.insert(arg)
        print("OK")

    elif cmd == "CONTAINS":
        if root.contains(arg):
            print("YES")
        else:
            print("NO")

    elif cmd == "SIZE":
        print(root.size())

print("\n".join(out))
