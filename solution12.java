class Solution {
     public int divide(int div, int dis) {
        if (div == Integer.MIN_VALUE && dis == -1) return Integer.MAX_VALUE; 
        boolean negative = div < 0 ^ dis < 0; 
        div = Math.abs(div);
        dis = Math.abs(dis);
        int qut = 0, sub = 0;
        while (div - dis >= 0) {
            for (sub = 0; div - (dis << sub << 1) >= 0; sub++);
            qut += 1 << sub; 
            div -= dis << sub; 
        }
        return negative ? -qut : qut;
    }
}