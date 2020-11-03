class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        int cost = 0;
        WeightedUF uf = new WeightedUF(n);
        PriorityQueue<Edge> pq = new PriorityQueue<Edge>();

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int distance = distance(points[i], points[j]);
                pq.add(new Edge(i, j, distance));
            }
        }

        while (!pq.isEmpty() && uf.count() > 1) {
            Edge e = pq.poll();
            int either = e.either(), other = e.other(either);
            if (uf.union(either, other)) cost += e.weight();
        }

        return cost;
    }

    private int distance(int[] pointA, int[] pointB) {
        return Math.abs(pointA[0] - pointB[0]) + Math.abs(pointA[1] - pointB[1]);
    }

    private class WeightedUF {
        private final int[] ids;
        private int[] size;
        private int count;

        public WeightedUF(int n) {
            ids = new int[n];
            for (int i = 0; i < n; i++) ids[i] = i;

            size = new int[n];
            for (int j = 0; j < n; j++) size[j] = 1;

            count = n;
        }

        public boolean union(int p, int q) {
            int parentP = find(p);
            int parentQ = find(q);

            if (parentP == parentQ) return false;

            if (size[parentP] > size[parentQ]) {
                ids[parentQ] = parentP;
                size[parentP] += size[parentQ];
            } else {
                ids[parentP] = parentQ;
                size[parentQ] += size[parentP];
            }

            count--;
            return true;
        }

        public int find(int p) {
            while (p != ids[p]) {
                ids[p] = ids[ids[p]];
                p = ids[p];
            }

            return p;
        }

        public int count() {
            return count;
        }
    }

    private class Edge implements Comparable<Edge> {
        private final int v;
        private final int w;
        private final int weight;

        public Edge (int v, int w, int weight) {
            this.v = v;
            this.w = w;
            this.weight = weight;
        }

        public int either() {
            return v;
        }

        public int other(int vertex) {
            if (vertex == v) return w;
            else if (vertex == w) return v;
            else throw new RuntimeException("Inconsistent edge");
        }

        public int weight() {
            return weight;
        }

        public int compareTo(Edge that) {
            return Integer.compare(weight, that.weight);
        }
    }
}