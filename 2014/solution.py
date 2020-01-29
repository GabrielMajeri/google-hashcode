from functools import partial

with open("example.txt") as f:
    line = f.readline()
    node_count, edge_count, max_time, cars, start_node = map(int, line.split())

    positions = [(0.0, 0.0)] * node_count
    for node in range(node_count):
        line = f.readline()
        latitude, longitude = map(float, line.split())
        positions[node] = (latitude, longitude)

    graph = {}
    for edge in range(edge_count):
        line = f.readline()
        start, end, bidir, cost, length = map(int, line.split())
        graph[(start, end)] = (cost, length)
        if bidir:
            graph[(end, start)] = (cost, length)

# The routes taken by each car
routes = [
    [0],
    [0, 1, 2],
]

# Print the solution to be able to later inspect it manually
with open("output.txt", "w") as f:
    # Bind print to the output file to shorten calls
    fprint = partial(print, file=f)

    fprint(len(routes))
    for route in routes:
        fprint(len(route))
        for junction in route:
            fprint(junction)

with open("output.txt") as f:
    total_score = 0

    solution_cars = int(f.readline())
    assert solution_cars == cars

    # Remember which streets were visited by any car at any point
    visited = set()

    for _ in range(solution_cars):
        itinerary_length = int(f.readline())
        car_time = 0

        current_node = int(f.readline())
        assert current_node == start_node, "Not starting in correct junction"

        for stop in range(1, itinerary_length):
            target_node = int(f.readline())

            edge = (current_node, target_node)
            assert edge in graph, "Inexistent street"

            cost, length = graph[edge]
            car_time += cost
            assert car_time < max_time, "Car takes too much time"

            # Add the street's length to our total score
            # if it hasn't been visited before
            if edge not in visited:
                total_score += length

            visited.add(edge)
            visited.add((target_node, current_node))

            # Keep traversing the itinerary
            current_node = target_node

    print("Score:", total_score)
