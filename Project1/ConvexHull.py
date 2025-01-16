import math
import sys
import random
import time


EPSILON = sys.float_info.epsilon

'''
Given two points, p1 and p2,
an x coordinate, x,
and y coordinates y3 and y4,
compute and return the (x,y) coordinates
of the y intercept of the line segment p1->p2
with the line segment (x,y3)->(x,y4)
'''
def yint(p1, p2, x, y3, y4):
	x1, y1 = p1
	x2, y2 = p2
	x3 = x
	x4 = x
	px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / \
		 float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
	py = ((x1*y2 - y1*x2)*(y3-y4) - (y1 - y2)*(x3*y4 - y3*x4)) / \
			float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3-x4))
	return (px, py)

'''
Given three points a,b,c,
computes and returns the area defined by the triangle
a,b,c. 
Note that this area will be negative 
if a,b,c represents a clockwise sequence,
positive if it is counter-clockwise,
and zero if the points are collinear.
'''
def triangleArea(a, b, c):
	return (a[0]*b[1] - a[1]*b[0] + a[1]*c[0] \
                - a[0]*c[1] + b[0]*c[1] - c[0]*b[1]) / 2.0;

'''
Given three points a,b,c,
returns True if and only if 
a,b,c represents a clockwise sequence
(subject to floating-point precision)
'''
def cw(a, b, c):
	return triangleArea(a,b,c) < EPSILON;
'''
Given three points a,b,c,
returns True if and only if 
a,b,c represents a counter-clockwise sequence
(subject to floating-point precision)
'''
def ccw(a, b, c):
	return triangleArea(a,b,c) > EPSILON;

'''
Given three points a,b,c,
returns True if and only if 
a,b,c are collinear
(subject to floating-point precision)
'''
def collinear(a, b, c):
	return abs(triangleArea(a,b,c)) <= EPSILON

'''
Given a list of points,
sort those points in clockwise order
about their centroid.
Note: this function modifies its argument.
'''
def clockwiseSort(points):
	# get mean x coord, mean y coord
	xavg = sum(p[0] for p in points) / len(points)
	yavg = sum(p[1] for p in points) / len(points)
	angle = lambda p:  ((math.atan2(p[1] - yavg, p[0] - xavg) + 2*math.pi) % (2*math.pi))
	points.sort(key = angle)

'''
Replace the implementation of computeHull with a correct computation of the convex hull
using the divide-and-conquer algorithm
'''
def findRightMostPoint(convexHull): 
	if not convexHull:
		raise ValueError("convexHull is empty")
	rightMostIndex = 0
	rightMostX = convexHull[0][0]
	length = len(convexHull)
	for i in range(1,length):
		x = convexHull[i][0] #Get x coordinate of current point
		if x > rightMostX: 
			rightMostIndex = i #if this is the point with the greatest x coord, return as rightmost index
			rightMostX = x 
	return rightMostIndex

def findLeftMostPoint(convexHull):
	if not convexHull:
		raise ValueError("convexHull is empty")
	leftMostIndex= 0
	leftMostX = convexHull[0][0]
	length = len(convexHull)
	for i in range(1, length):
		x= convexHull[i][0] #get the x coord of current point
		if x < leftMostX:
			leftMostIndex = i #if this is the point with least x coord, return as leftmost index
			leftMostX = x
	return leftMostIndex

def isUpperTangent(aPoint, bPoint, points):
	for point in points:
		if point == aPoint or point ==bPoint:
			continue #skip if this is our points
		#If any point is not clockwise/is counterclockwise nor collinear to this segment, then these are not the uppertangent points
		if not(cw(aPoint, bPoint, point) or collinear(aPoint,bPoint,point)): 
			return False  
	return True

def isLowerTangent(aPoint, bPoint,points):
	for point in points:
		if point == aPoint or point == bPoint:
			continue
		#If any point is not counterclockwise/is clockwise nor collinear to this segment, then these are not the lowertangent points
		if not(ccw(aPoint, bPoint, point) or collinear(aPoint,bPoint,point)):
			return False
		return True

def merge(hullA, hullB):
    if not hullA or not hullB:
        raise ValueError("Both hulls must be non-empty to merge.")

    rightMostIndexA = findRightMostPoint(hullA)
    leftMostIndexB = findLeftMostPoint(hullB)

    # Find lower tangent
    indexA, indexB = rightMostIndexA, leftMostIndexB
    while True:
        updated = False
        while not isLowerTangent(hullA[indexA], hullB[indexB], hullA):
            indexA = (indexA - 1) % len(hullA)
            updated = True
        while not isLowerTangent(hullA[indexA], hullB[indexB], hullB):
            indexB = (indexB + 1) % len(hullB)
            updated = True
        if not updated:
            break
    lowerIndexA, lowerIndexB = indexA, indexB

    # Find upper tangent
    indexA, indexB = rightMostIndexA, leftMostIndexB
    while True:
        updated = False
        while not isUpperTangent(hullA[indexA], hullB[indexB], hullA):
            indexA = (indexA + 1) % len(hullA)
            updated = True
        while not isUpperTangent(hullA[indexA], hullB[indexB], hullB):
            indexB = (indexB - 1) % len(hullB)
            updated = True
        if not updated:
            break
    upperIndexA, upperIndexB = indexA, indexB

    # Construct merged hull
    mergedHull = []

    # Add points from hullB between lowerIndexB and upperIndexB
    indexB = lowerIndexB
    while True:
        mergedHull.append(hullB[indexB])
        if indexB == upperIndexB:
            break
        indexB = (indexB + 1) % len(hullB)

    # Add points from hullA between upperIndexA and lowerIndexA
    indexA = upperIndexA
    while True:
        mergedHull.append(hullA[indexA])
        if indexA == lowerIndexA:
            break
        indexA = (indexA + 1) % len(hullA)

    return mergedHull

def computeHullNaive(points):
	#Base case
	if len(points) <=3:
		return points
	convexHull = set()
	#Checks all pairs of points
	for point1 in points:
		for point2 in points:
			if point1==point2:
				continue#skip if same point
			#Assume this is a valid edge initially
			validEdge = True
			side = None
			for point3 in points:
				if point3 == point1 or point3== point2:
					continue #skip[] if same point
				#Checks all the points after establishing p1 and p2 to see if this is a valid convex edge
				orientation = cw(tuple(point1),tuple(point2),tuple(point3))
				if side is None:
					side = orientation
				elif side != orientation and not collinear(tuple(point1),tuple(point2),tuple(point3)):
					validEdge = False
					break
			if validEdge is True:
				convexHull.add(tuple(point1))
				convexHull.add(tuple(point2))
	convexHull = list(convexHull)
	clockwiseSort(convexHull)
	return convexHull
					
def computeHull(points):

	
	points = list(set(points))

	if len(points) <= 50:
		return computeHullNaive(points)
	if len(points) <= 3:  # Base case: 3 or fewer points form a convex hull
		return points
    # Sort points and split into left and right subsets
	points.sort(key=lambda p: p[0])
	mid = len(points) // 2
	left = points[:mid]
	right = points[mid:]
	if not left or not right:  # Ensure subsets are non-empty
		raise ValueError("Left or right subset is empty in computeHull")
	
	leftHull = computeHull(left)
	rightHull = computeHull(right)

	return merge(leftHull, rightHull)




def generatePoints(num_points, xRange=(0, 1000), yRange=(0, 1000)):
	#list to hold points
	points = []
	for _ in range(num_points):
		x= random.randint(xRange[0], xRange[1])
		y=random.randint(yRange[0], yRange[1])
		points.append((x,y))
	return points

#Benchmarks
if __name__ == "__main__":
	numPointsList = [10, 100, 1000, 5000, 10000,50000] #input sizes
	naiveTimes = []
	divideConquerTimes=[]

	for numPoints in numPointsList:
		points = generatePoints(numPoints)

		#Benchmark the naive implementation
		startTime = time.time()
		computeHull(points)
		divideConquerTimes.append(time.time()-startTime)

		print(numPoints, "Time is done")

	print(divideConquerTimes)



   

    


