# 🔍 Search Algorithms

## 🎯 Objectives

- **Understand** the differences between various search algorithms

## 🔍 What is the goal of a search algorithm?

Search algorithms find a path from a starting point to a pre-defined ending point.  It is not sufficient to find the ending point, but the algorithm must determine the *path* to get from the start to the end. 

One of the simplest ways to visual the algorithms is to look at some kind of map, divided into a grid, with various obstacles between the start and the end.

In a simple map configuration, we can move one cell at a time in the `UP`, `DOWN`, `LEFT` and `RIGHT` directions. 

Map search algorithms use a systematic method of visiting cells, by proceeding according to the rules of movement.  The search will proceed until the goal is found, or there is no more cells that can be reached from the start using these moves. If search finds the goal, we say that it's _reachable_ and the algorithm outlines a path, or sequence of moves, to reach the goal.

![Path](/Users/sandy/Documents/GitHub/cs4p6/asg/asg3/starter/images/1-Path.png)



## Depth-first Search (DFS)

Starting from the **start** cell, the first strategy is to visit each of the cells in the following way, called _depth-first_. This search strategy continues in one direction until there is nowhere else to go. It then goes back the way it came, called _backtracking_, and tries the next available direction with the same strategy. It's
behaviour can be modelled with a `Stack`.

> DFS does NOT find the shortest path from the start to the end.

**Algorithm**

* From the current position, try going `UP`.  If you can't go up, go `RIGHT`, and if you can't, try `DOWN`, and finally, try `LEFT`.  Do not go to any cell that you have already been to. 
  * Keep track of the moves that you are using to get to each cell.
  * Stop if you have found the `goal`
  * If you are able to move, repeat above process.
  
* If you cannot move to a new cell that has not already been visited (coloured grey in the diagram below) or is an obstacle, then
  * backup to the previous cell.
  * check to see if another direction is from here is alright.  If not back up again, repeat.

The following sequence of terrains show a DFS step-by-step:

* Cell `0,0`
  * Try moving `UP`, can't. Try `RIGHT`, yes, move to `1,0`
  
* Cell `1,0`
  * Try moving `UP`, can't. Try `RIGHT`, yes, move to `2,0`
  
* Cell `2,0`
  * Try moving `UP`, can't. Try `RIGHT` (Wall),, `DOWN` (Wall),  `LEFT` (been there already)
  * Go back to cell `1,0`
  
* Cell `1,0`
  * Try moving `UP`, can't. Try `RIGHT`, (been there already), `DOWN` (Wall),  `LEFT` (been there already) 
  * Go back to previous cell `0,0`
  
* Cell `0,0`
  * Try moving `UP`, can't. Try `RIGHT` (been there already), `DOWN` to cell `0,1`
  
* *etc*

![DFS](/Users/sandy/Documents/GitHub/cs4p6/asg/asg3/starter/images/2-DFS.png)

## Breadth-First Search (BFS)

Starting from the **start** cell, the second strategy is to visit each of the cells in the following way, called a _breadth first_. Cell is visited in the order they are discovered, so the search strategy expands outwards from the starting cell in layers, like an onion. For example, the search will visit all cells 2 moves from the start before visiting cells that are 3 moves from the start. It's behaviour can be modelled with a `Queue`.

> BFS will find a path that is as short as possible

**Algorithm**

* From the current cell, 
  * find all of your neighbours
  * Ignore any neighbour that you have already placed in the queue 
  * Store the neighbour information in a `queue` 
  * Keep track of the direction that each neighbour is from the current cell

* Mark the current cell as `seen`.
* For each cell in the `queue`, repeat the process until you find the `goal`

The following sequence of terrains show a BFS step-by-step:

* Cell `0,0`
  * Add neighbours to `queue = [ 1,0  0,1 ]` (coloured grey in the diagram)
  * Mark current cell as `seen` (coloured black in the diagram) (`seen = [ 0,0 ]`)
  * Go to the next neighbour **(`1,0`)** (`queue = [ 0,1 ]`)
  
* Cell `1,0`
  * Add neighbours `2,0` to `queue = [ 0,1, 2,0 ]`
  * Mark current cell as `seen` (`seen = [ 0,0 1,0]`)
  * Go to the next neighbour **(`0,1`)** (`queue = [ 2,0 ]`)

* Cell `0,1`
  * Add neighbours `0,2` to `queue = [ 2,0 0,2 ]`
  * Mark current cell as `seen` (`seen = [ 0,0  1,0  0,1 ]`)
  * Go to the next neighbour **(`2,0`)**  (`queue = [ 0,2 ]`)

* Cell `2,0`
  * No neighbours: (`1,0`) has already been `seen`.
  * Mark current cell as `seen` (`seen = [ 0,0  1,0  0,1  2,0 ]`)
  * Go to the next neighbour **(`0,2`)**  (`queue = [ ]`)

* *etc*

![BFS](/Users/sandy/Documents/GitHub/cs4p6/asg/asg3/starter/images/3-BFS.png)

## 📍 Paths

If a search successfully finds the goal cell from the start cell, we want to be able to return the path from the start the goal. To do so, it is necessary to keep track of the directions from one cell to another.

