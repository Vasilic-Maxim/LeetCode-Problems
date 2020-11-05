import java.util.PriorityQueue;

class Solution {
    public int minimumEffortPath(int[][] h) {
        int rows = h.length;
        int cols = h[0].length;
        int totalCells = rows * cols;
        if (totalCells == 1) return 0;

        // Add all possible edges to the priority queue.
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (i + 1 < rows) pq.add(createEdge(h, i, j, i + 1, j));
                if (j + 1 < cols) pq.add(createEdge(h, i, j, i, j + 1));
            }
        }

        // While source and sink are not connected, take an
        // edge from priority queue and do the union operation
        // in Union-Find data structure.
        UF uf = new UF(totalCells);
        int source = 0, sink = totalCells - 1;
        Edge edge = null;
        while (uf.find(source) != uf.find(sink)) {
            edge = pq.poll();
            uf.union(edge.from(), edge.to());
        }

        return edge.weight();
    }

    private Edge createEdge(int[][] heights, int i1, int j1, int i2, int j2) {
        int weight = Math.abs(heights[i1][j1] - heights[i2][j2]);
        int from = heights[0].length * i1 + j1;
        int to = heights[0].length * i2 + j2;
        return new Edge(from, to, weight);
    }

    private static class Edge implements Comparable<Edge> {
        private final int from, to, weight;

        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }

        public int from() {
            return from;
        }

        public int to() {
            return to;
        }

        public int weight() {
            return weight;
        }

        public int compareTo(Edge that) {
            return Integer.compare(this.weight, that.weight);
        }
    }

    private static class UF {
        private final int[] ids, sizes;
        private int count;

        public UF(int n) {
            ids = new int[n];
            for (int i = 0; i < n; i++)
                ids[i] = i;

            sizes = new int[n];
            for (int j = 0; j < n; j++)
                sizes[j] = 1;

            count = n;
        }

        public void union(int p, int q) {
            int parentP = find(p);
            int parentQ = find(q);
            if (parentP == parentQ) return;

            if (sizes[parentP] > sizes[parentQ]) {
                ids[parentQ] = parentP;
                sizes[parentP] += sizes[parentQ];
            } else {
                ids[parentP] = parentQ;
                sizes[parentQ] += sizes[parentP];
            }

            count--;
        }

        public int find(int p) {
            while (p != ids[p]) {
                ids[p] = ids[ids[p]];
                p = ids[p];
            }

            return p;
        }
    }
}