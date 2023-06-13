from zad8testy import runtests
from queue import deque
from queue import PriorityQueue

def plan(T):
    m = len(T[0])
    counter = 1

    def get_fuel(T, column):
        if (T[0][column] == 0):
            return 0

        n = len(T[0])
        m = len(T)
        fuel = 0
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        queue.append((0 , column))
        fuel += T[0][column]
        T[0][column] = 0
        while queue:
            position = queue.popleft()
            for neighbour in neighbours:
                ac_x = position[1] + neighbour[1]
                ac_y = position[0] + neighbour[0]
                if ac_x < 0 or ac_y < 0 or ac_x >= n or ac_y >= m:
                    continue
                if T[ac_y][ac_x] != 0:
                    queue.append((ac_y, ac_x))
                    fuel += T[ac_y][ac_x]
                    T[ac_y][ac_x] = 0
        return fuel
    ac_range = get_fuel(T, 0)
    prev_range = 0
    queue = PriorityQueue()
    while ac_range < m - 1:
        for i in range(prev_range, ac_range + 1):
            for_queue = get_fuel(T, i)
            if for_queue != 0:
                queue.put((-for_queue, for_queue))
        prev_range = ac_range
        ac_range += queue.get()[1]
        counter += 1

    return counter

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )