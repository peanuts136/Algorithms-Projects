# Algorithms-Projects
A collection of algorithm projects which demonstrtates key principles used in algorithms
## Table of Contents 
- [Overview](#overview)
- [Projects](#projects)
  - [1. Convex Hull Problem](#1-convex-hull-problem)
  - [2. Gene Sequencing Problem](#2-gene-sequencing-problem)
  - [3. Loaded vs. Fair Die Problem](#3-loaded-vs-fair-die-problem)
- [Resources](#resources)

---

## Overview
These projects are meant to utilize learned algorithm principles and apply them into various coding problems

---

## Projects
### 1. Convex hull problem
Given a group of points, how are we able to create a closed shape using those points such that it creates "the intersection of all convex sets containing a given subset of a Euclidean space" - Wiki.
  > *“Imagine wrapping a rubber band around the outside of a group of points—that outline is the convex hull.”*
#### Key Details
  -The convex hull algorithm is meant to utilize the divide and conquer approach to split up the work in order to get the convex hull of a group of given points. This is then compared with a naive approach where we take into consideration every      possible pair of points and see if they satisfy convexity conditions. The convex hull problem itself revolves around finding the smallest convex polygon that encloses a given set of points in a 2D plane
  -  Utilizes the divide and conquer approach, dividing the given points into subproblems of 2 or 3 preferably.
  -  Naive approach checks every possible pair and tripletes of points in order to main convecity 
  -  The theoretical runtime should be nlogn. 

  
### 2. Gene sequencing problem
Given 2 or more sequences, how can we determine the similarity between them in order to determine how closely related they are
#### Subproblems / Algorithms 
  - Global alignement: A global alignment tries to align all of one sequence with all of the other, from end to end.
  - Local alignment: A local alignment finds subregions (subsequences) of each sequence that align best, rather than forcing an alignment across the entire lengths.
  - Affine alignment: utilizes a special affine gap penalty function instead of the linear gap functions in the other functions, meaning that opening a new gap costs more, but extending the gap will be less costly.
  - PAM120 Script: (Point Accepted Mutation) substitution matrices which are used in all of the given algorithms to determine how likely it is that one amino acid would be substituted for another in evolution.

### 3. Loaded vs. Fair Die problem
By analyzing the rolls of a fair vs loaded die, HMMs can be utilized in order to infer hidden states of Fair or Loaded
#### Algorithms 
 - Viterbi: outputs the most problem sequence of hidden states based on observable events, useful to find a *single best path*
 - Forward-Backward: outputs the marginal probability for each time step, useful to capturing the *uncertainty* at any point
  
---

### Resources
The following links are the data analyzation docs of each of the projects and problems
  -  [Convex Hull](https://docs.google.com/document/d/1AeBn_ufy2NXda0Ij5n7mWwq5LuSZ-Va_t9op4bTcUuA/edit?usp=sharing)
  - [Gene Sequencing](https://docs.google.com/document/d/1Xr2hXBsGU0QzhebSXnkhfqyUHGSpO4ZEZOzxjIVF-c8/edit?usp=sharing)
  - [Loaded vs. Fair Die](https://docs.google.com/document/d/1_q0R1-LTI5npcNLo-3DWWSD6nxCBJnBlbxCyD5rb9FM/edit?usp=sharing)
