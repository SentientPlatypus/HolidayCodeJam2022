our_graph = {
    1:[9, 8],
    2:[2,9],
    3:[2],
    4:[3],
    5:[4],
    6:[5,9],
    7:[6],
    8:[8],
    9:[1,2,6,10],
    10:[11],
    11:[10, 12],
    12:[11, 13],
    13:[14],
    14:[15, 24],
    15:[16, 18, 22, 14],
    16:[15, 17],
    17:[18],
    18:[15, 19],
    19:[20],
    20:[21],
    21:[22],
    22:[23, 15],
    23:[16],
    24:[25],
    25:[26],
    26:[12],
    
}


def shortestDistance(start:int, end:int) ->int:
    queue= []
    distances = {}
    queue.append(start)
    distances[start] = 0


    if start == end:
        return 0
    
    while True:
        current = queue.pop(0)
        for node in our_graph[current]:
            queue.append(node)
            distances[node] = distances[current] + 1
            if node == end:
                return distances[node]
    return None

print(shortestDistance(20,25))

    



