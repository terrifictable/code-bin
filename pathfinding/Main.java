package com.terrific;

public class Main {

    public static void main(String[] args) {
        // BFS and DFS difference
        /* BDF = Traverse a graph level by level
         *       Utilizes a Queue
         *       Better if destination is on average close to start
         *       Siblings are visited before children */

        /* DFS = Traverse a graph branch by branch
         *       Utilizes a Stack
         *       Better if destination is on average far from start
         *       Children are visited before siblings
         *       More popular for games/puzzles */


        Graph graph = new Graph(5);

        graph.addNode(new Node('A'));
        graph.addNode(new Node('B'));
        graph.addNode(new Node('C'));
        graph.addNode(new Node('D'));
        graph.addNode(new Node('E'));

        graph.addEdge(0, 1);
        graph.addEdge(1, 2);
        graph.addEdge(2, 3);
        graph.addEdge(2, 4);
        graph.addEdge(4, 0);
        graph.addEdge(4, 2);

        graph.print();
        // graph.depthFirstSearch(1);
        graph.breadthFirstSearch(1);
    }
}
