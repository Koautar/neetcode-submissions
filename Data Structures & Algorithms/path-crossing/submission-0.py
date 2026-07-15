class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }

        visited = {(0, 0)}
        x, y = 0, 0

        for position in path:
            dx, dy = direction[position]
            x = x + dx
            y = y + dy

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False