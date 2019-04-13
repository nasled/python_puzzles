import math

ROUND = 10

def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    if numDeliveries > numDestinations:
        exit('Error')

    distances = {}
    for i in allLocations:
        x = i[0]
        y = i[1]
        distance = round(math.sqrt(math.pow(x, 2) + math.pow(y, 2)), ROUND)
        distances[distance] = i
    sorted_distances = sorted(distances)

    result = []
    for j in range(numDeliveries):
        distance = sorted_distances[j]
        coordinates = distances[distance]
        result.append(coordinates)

    return result

# ClosestXdestinations(3, [[1,-3], [1,2], [3,4]], 1)
ClosestXdestinations(3, [[1,2], [3,4], [1,-1]], 2)