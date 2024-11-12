from collections import deque

def min_dice_throws(n, moves):
    visited = [False] * n
    queue = deque([(0, 0)])  # (position, throws)
    visited[0] = True

    while queue:
        pos, throws = queue.popleft()

        if pos == n - 1:
            return throws

        for i in range(1, 7):
            next_pos = pos + i
            if next_pos < n and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((moves[next_pos] if moves[next_pos] != -1 else next_pos, throws + 1))

    return -1

# Test with 30 positions and sample ladder/snake configuration
board_size = 30
moves = [-1] * board_size
moves[2] = 11  # Ladder
moves[4] = 29   # Ladder
moves[10] = 15  # Ladder
moves[19] = 28  # Ladder
moves[26] = 3  # Snake
moves[20] = 12   # Snake
moves[16] = 1   # Snake

print(min_dice_throws(board_size, moves))
