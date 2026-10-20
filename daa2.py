
import heapq

# Node of Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Compare nodes by frequency
    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman Codes
def generate_codes(root, code, huffman_codes):
    if root is None:
        return

    # Leaf node represents a character
    if root.char is not None:
        huffman_codes[root.char] = code if code else "0"
        return

    generate_codes(root.left, code + "0", huffman_codes)
    generate_codes(root.right, code + "1", huffman_codes)


# Build Huffman Tree using Greedy Strategy
def huffman_encoding(chars, freqs):
    min_heap = []

    for char, freq in zip(chars, freqs):
        heapq.heappush(min_heap, Node(char, freq))

    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(min_heap, merged)

    root = min_heap[0]
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    return huffman_codes


# Main Program
n = int(input("Enter the number of characters: "))

chars = []
freqs = []

for i in range(n):
    char = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    chars.append(char)
    freqs.append(freq)

if n <= 0 or any(freq <= 0 for freq in freqs):
    print("Enter at least one character with positive frequencies.")
elif len(set(chars)) != len(chars):
    print("Characters must be unique.")
else:
    codes = huffman_encoding(chars, freqs)

    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(char, ":", code)
