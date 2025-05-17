from queue import PriorityQueue

def a_star(grid, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
        for dx, dy in neighbors:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative = g_score[current] + 1
                if neighbor not in g_score or tentative < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative
                    f_score = tentative + heuristic(neighbor, goal)
                    open_set.put((f_score, neighbor))
    return None

grid = [[0]*10 for _ in range(10)]
grid[5][3:7] = [1]*4
path = a_star(grid, (0,0), (9,9))
print("Path:", path)