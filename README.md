# Metaheuristic Algorithms
## TSP - Traveling Salesman Problem 
is an algorithmic problem tasked with finding the shortest route between a set of points and locations  
that must be visited. In the problem statement, the points are the cities a salesperson might visit.

We implemented algorithms such as:  

- **k-random**    
> A greedy algorithm is a general term for algorithms that try to add the lowest cost possible in each iteration,   
> even if they result in sub-optimal combinations.   
> Complexity: $O(k*n)$

- **Nearest Neighbour**  
> The nearest neighbor heuristic is another greedy algorithm, or what some may call naive. It starts at one city  
> and connects with the closest unvisited city. It repeats until every city has been visited. It then returns to the starting city.  
> Complexity: $O(n^2)$  

- **Nearest Neighbour Extended**  
> Better NN, which differ from NN of choosing start point.  
> Complexity: $O(n^2)$  

- **2-OPT**  
> It's a simple local search algorithm. Building the new route and calculating the distance of the new route can be
> a very expensive operation, usually $O(n)$ where n is the number of vertices in the route. This can sometimes be 
> skipped by performing a $O(1)$ operation. Since a 2-opt operation involves removing 2 edges and adding 2 different
> edges we can subtract and add the distances of only those edges.  

- **GA**  
> Genetic Algorithm for Traveling Salesman Problem with Modified Cycle Crossover Operator.  

It was group project. We wrote it in pair. We did a lot of tests and charts. We were using tsplib and tests instances.
