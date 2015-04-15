# Lyft programming challenge solution
# By Andy Nelson

import math

# Finds the great circle distance between two latitude/longitude pairs (as
# tuples or lists) on the earth's surface.
def findCircDist(pointA, pointB):

    # Convert the latitude and longitude values to radians
    latA = math.radians(pointA[0])
    latB = math.radians(pointB[0])
    longA = math.radians(pointA[1])
    longB = math.radians(pointB[1])
    deltaLat = latA - latB
    deltaLong = longA - longB

    # Use the great circle distance formula to find the distance between the
    # two points
    angle = math.atan2(math.sqrt(math.pow((math.cos(latB) *
                                           math.sin(deltaLong)), 2) +
                                 math.pow((math.cos(latA) * math.sin(latB) -
                                           math.sin(latA) * math.cos(latB) *
                                           math.cos(deltaLong)), 2)),
                    (math.sin(latA) * math.sin(latB) + math.cos(latA) *
                     math.cos(latB) * math.cos(deltaLong)))

    return 3958.76 * angle

# Determines the shorter of two detour distances, given two start and two end
# points (latitude/longitude pairs) as tuples or lists.
def findDetourDist(startA, endA, startB, endB):

    # Determine the two detour distances
    detourA = (findCircDist(startA, startB) + findCircDist(startB, endB) +
              findCircDist(endB, endA) - findCircDist(startA, endA))
    detourB = (findCircDist(startB, startA) + findCircDist(startA, endA) +
              findCircDist(endA, endB) - findCircDist(startB, endB))

    # Return whichever detour distance is shorter
    if detourB >= detourA:
        return detourA
    else:
        return detourB
