import sys

from radix_trie import RadixTrie
from trie import Trie

root = Trie()
size_count = 0

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line: continue
    parts = line.split(" ")
    cmd = parts[0]; arg = parts[1] if len(parts) > 1 else ""; arg2 = parts[2] if len(parts) > 2 else ""
    if cmd == "INSERT":
        root.insert(arg)

    elif cmd == "INSERT_N":
        root.insert(arg, int(arg2))

    elif cmd == "CONTAINS":
        if root.contains(arg):
            print("YES")
        else:
            print("NO")

    elif cmd == "DELETE":
        root.delete(arg)

    elif cmd == "SUGGEST":
        results = root.suggest(arg, int(arg2))
        if len(results) == 0:
            print("none")
        else:
            print(','.join([str(result) for result in results]))

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