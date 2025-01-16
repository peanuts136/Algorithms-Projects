# Algorithms-Projects
##These projects are meant to utilize learned algorithm principles and apply them into various coding problems

###There are 3 main projects
- 1. Convex hull problem: given a group of points, how are we able to create a closed shape using those points such that it creates "the intersection of all convex sets containing a given subset of a Euclidean space" - Wiki.
  The convex hull algorithm is meant to utilize the divide and conquer approach to split up the work in order to get the convex hull of a group of given points. This is then compared with a naive approach where we take into consideration every      possible pair of points and see if they satisfy convexity conditions. The convex hull problem itself revolves around finding the smallest convex polygon that encloses a given set of points in a 2D plane
  -  In laymans terms, what would be the shape created if one wraps a rubber band around a group of points.
  -  Utilizes the divide and conquer approach, dividing the given points into subproblems of 2 or 3 preferably. 
  -  Should have a theorectical runtime of nlogn
  -  [Google Docs](https://docs.google.com/document/d/1AeBn_ufy2NXda0Ij5n7mWwq5LuSZ-Va_t9op4bTcUuA/edit?usp=sharing)
  
- 2. Gene sequencing problem: given 2 or more sequences, how can we determine the similarity between them in order to determine how closely related they are
  There are 3 algorithms within this project, 
  - Global alignement: A global alignment tries to align all of one sequence with all of the other, from end to end.
  - Local alignment: A local alignment finds subregions (subsequences) of each sequence that align best, rather than forcing an alignment across the entire lengths.
  - Affine alignment: utilizes a special affine gap penalty function instead of the linear gap functions in the other functions, meaning that opening a new gap costs more, but extending the gap will be less costly.
  - 
  -[Google Docs](https://docs.google.com/document/d/1Xr2hXBsGU0QzhebSXnkhfqyUHGSpO4ZEZOzxjIVF-c8/edit?usp=sharing)
