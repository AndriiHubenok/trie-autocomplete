import sys

from trie import Trie

root = Trie()
size_count = 0

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line: continue
    parts = line.split(" ", 1)
    cmd = parts[0]; arg = parts[1] if len(parts) > 1 else ""
    if cmd == "INSERT":
        root.insert(arg)

    elif cmd == "CONTAINS":
        if root.contains(arg):
            print("YES")
        else:
            print("NO")

    elif cmd == "DELETE":
        root.delete(arg)

    elif cmd == "SIZE":
        print(root.size())

    elif cmd == "FREQ":
        print(root.freq(arg))

    elif cmd == "NODES":
        print(root.nodes())

    elif cmd == "PREFIX":
        results = root.prefix(arg)
        results.sort()
        if len(results) == 0:
            print("none")
        else:
            print(','.join(results))