# https://www.youtube.com/watch?v=JSZ8sE8UP6g
import math

coords = [[0, 0], [5, 6], [2, 10], [7, 6]]


def array2d(coords: list, char: str, xamp=1, yamp=1):
    result = []
    for x, y in coords:
        result.append("\n"*(y*yamp).__round__() +
                      " "*(x*xamp).__round__() +
                      char)
    return result


class Pathfinder:
    def __init__(self, coords: list, conf: int, xamp=1, yamp=1) -> None:
        self.coords = coords
        self.conf = conf
        self.xamp = xamp
        self.yamp = yamp

    def get_next_point(self, dist_to_start: list):
        distances = []
        for i, distance in enumerate(dist_to_start):
            try:
                p2 = dist_to_start[i+1]
            except:
                break
            a1 = math.sqrt((distance[0]-p2[0])**2)
            a2 = math.sqrt((distance[1]-p2[1])**2)
            distances.append(a1+a2)
        return distances

    def get_fastest_way(self, distances: list):
        distance = []
        for _ in range(len(distances)):
            smallest = distances[0]
            for i in range(0, len(distances), 1):
                if (distances[i] < smallest):
                    smallest = distances[i]

            distances.remove(smallest)
            distance.append(smallest)
        return distance

    def calc_points(self, distances, smallest):
        points = []
        for x in smallest:
            points.append(distances.index(x)+1)
        return points


pathfinder = Pathfinder(coords, 5, yamp=.2)
distances = pathfinder.get_next_point(coords)
smallest = pathfinder.get_fastest_way(distances)
distances = pathfinder.get_next_point(coords)
# points = pathfinder.calc_points(distances, smallest)
print("Distances: " + str(smallest))
# print("Points: " + str(points))
print(*array2d(coords, "X", yamp=.2))
