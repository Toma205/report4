import random

GRID_SIZE = 40
NUM_POINTS = 100
NUM_CLUSTERS = 10
MAX_ITERATIONS = 10

def generate_points(num_points, grid_size):
    return [(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(num_points)]

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def assign_clusters(points, centers):
    clusters = [[] for _ in centers]
    for point in points:
        distances = [manhattan_distance(point, center) for center in centers]
        nearest = distances.index(min(distances))
        clusters[nearest].append(point)
    return clusters

def update_centers(clusters):
    new_centers = []
    for cluster in clusters:
        if cluster:
            x_mean = int(sum(p[0] for p in cluster) / len(cluster))
            y_mean = int(sum(p[1] for p in cluster) / len(cluster))
            new_centers.append((x_mean, y_mean))
        else:
            new_centers.append((random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)))
    return new_centers

def visualize(points, centers):
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for x, y in points:
        grid[y][x] = '*'
    for x, y in centers:
        grid[y][x] = 'C'
    for row in grid:
        print(' '.join(row))

points = generate_points(NUM_POINTS, GRID_SIZE)
centers = generate_points(NUM_CLUSTERS, GRID_SIZE)

for _ in range(MAX_ITERATIONS):
    clusters = assign_clusters(points, centers)
    centers = update_centers(clusters)

print("\nFinal Clustering Visualization (C=Center, *=Point):\n")
visualize(points, centers)
