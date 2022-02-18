def isValid(img, row, col):
    return row > 0 and col > 0 and row < len(img) and col < len(img[0])


def neighbors(img, row, col, start):
    indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    return [(row, col) for row, col in indices
            if isValid(img, row, col) and img[row][col] == start]


def floodFill(img, row, col, p):
    """Returns ```input``` with the value of ```row, col``` changed to ```p```"""
    start = img[row][col]
    queue = [(row, col)]
    visited = set()

    while len(queue) > 0:
        row, col = queue.pop(0)
        visited.add((row, col))
        img[row][col] = p

        for row, col in neighbors(img, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return img


img = [[1, 0, 1, 1, 0],
       [0, 1, 0, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 1],
       [1, 0, 0, 0, 0]]
print("INPUT: ", end="")
print(*img)
print("RESULT: ", end="")
print(*floodFill(img, 2, 2, 2))

# IMG (0 = Black; 1 = White):
# https://cdn.discordapp.com/attachments/916092218761179198/944235675371327508/unknown.png
# 1, 0, 1, 1, 0
# 0, 1, 0, 1, 0
# 1, 1, 1, 1, 1
# 0, 0, 1, 0, 1
# 1, 0, 0, 0, 0

# Result (0 = Black, 1 = White, 2 = Yellow):
# https://cdn.discordapp.com/attachments/916092218761179198/944238735778807898/unknown.png
# 1, 0, 1, 1, 0
# 0, 2, 0, 2, 0
# 1, 2, 2, 2, 2
# 0, 0, 2, 0, 2
# 1, 0, 0, 0, 0
