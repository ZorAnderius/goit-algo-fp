graph = {
    'A': ['B','C','D'],
    'B': ['A','E','F','C'],
    'C': ['A','B', 'F', 'D'],
    'D': ['A', 'C', 'N', 'G'],
    'E': ['B', 'F', 'I'],
    'F': ['C', 'B', 'E', 'J', 'N'],
    'G': ['D', 'K', 'H'],
    'H': ['G', 'K'],
    'I': ['E', 'J', 'M', 'L'],
    'J': ['F', 'I', 'M', 'N'],
    'K': ['G', 'H', 'O'],
    'L': ['I', 'P'],
    'M': ['I', 'J', 'Q'],
    'N': ['F', 'J', 'R', 'O', 'D'],
    'O': ['K', 'N', 'S', 'T'],
    'P': ['L', 'Q', 'U'],
    'Q': ['M', 'P', 'R'],
    'R': ['N', 'Q', 'U'],
    'S': ['O', 'V', 'W'],
    'T': ['O', 'W'],
    'U': ['P', 'R', 'V'],
    'V': ['U', 'S'],
    'W': ['S', 'T'],
}