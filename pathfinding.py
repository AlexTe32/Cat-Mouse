import heapq

# Ја пресметува дистанцата измечу две цели
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Користиме А* за да го најдеме најбрзиот пат до Глушецот
# ( Искрено го гледав од YouTube па ќе повторим нешто што слушнав)
def a_star(start, goal, grid_rows, grid_cols, obstacles=set()):
    open_set = []
    heapq.heappush(open_set, (0 + manhattan(start, goal), 0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        # Кога ќе ја најдеме челта го врачаме патот
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        # Ги проверува сите цели до моментална целија
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dr, current[1] + dc)
            if 0 <= neighbor[0] < grid_rows and 0 <= neighbor[1] < grid_cols and neighbor not in obstacles:
                new_cost = cost + 1
                # Пресметува која целија е најблиску до целта и ја се поставува
                # Истовремено ја запишува целијата од каде е дојден
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + manhattan(neighbor, goal)
                    heapq.heappush(open_set, (priority, new_cost, neighbor))
                    came_from[neighbor] = current

    return []
