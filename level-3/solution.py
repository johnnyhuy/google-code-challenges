from collections import deque

def solution(maze):
    # Create visited arrays
    visited_with_wall = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited_without_wall = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    # Initialize queue and put starting node with zero distance
    queue = deque([(0, 0, 1, False)])  # (x, y, distance, is_wall_removed)

    while queue:
        x, y, dist, is_wall_removed = queue.popleft()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down

        # If we reached the end
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # If next position is within the maze
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                # If next cell is passable and not visited yet
                if not maze[nx][ny] and (not visited_with_wall[nx][ny] if is_wall_removed else not visited_without_wall[nx][ny]):
                    queue.append((nx, ny, dist + 1, is_wall_removed))
                    if is_wall_removed:
                        visited_with_wall[nx][ny] = True
                    else:
                        visited_without_wall[nx][ny] = True

                # If next cell is a wall and we haven't removed any wall yet
                elif maze[nx][ny] and not is_wall_removed and not visited_with_wall[nx][ny]:
                    queue.append((nx, ny, dist + 1, True))
                    visited_with_wall[nx][ny] = True

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
