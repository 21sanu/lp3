
import heapq

def huffman(chars, freq):
    heap = []
    count = 0

    for i in range(len(chars)):
        heapq.heappush(heap, (freq[i], count, chars[i]))
        count += 1

    while len(heap) > 1:
        f1, _, c1 = heapq.heappop(heap)
        f2, _, c2 = heapq.heappop(heap)

        heapq.heappush(heap, (f1 + f2, count, (c1, c2)))
        count += 1

    codes = {}

    def generate(tree, code=""):
        if isinstance(tree, str):
            codes[tree] = code if code else "0"
        else:
            generate(tree[0], code + "0")
            generate(tree[1], code + "1")

    generate(heap[0][2])
    return codes


n = int(input("Enter number of characters: "))

chars = []
freq = []

for i in range(n):
    chars.append(input("Enter character: "))
    freq.append(int(input("Enter frequency: ")))

codes = huffman(chars, freq)

print("Huffman Codes:")
for ch, code in codes.items():
    print(ch, ":", code)

