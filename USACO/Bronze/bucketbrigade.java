import java.io.*;
import java.util.*;

public class bucketbrigade {
    public static void main(String[] args) throws IOException
    {
        Kattio io = new Kattio("buckets");

        int barnX = 0, barnY = 0, rockX = 0, rockY = 0, lakeX = 0, lakeY = 0;

        for (int i = 0; i < 10; i++)
        {
            String row = io.next();
            for (int j = 0; j < 10; j++)
            {
                if (row.charAt(j) == 'B')
                {
                    barnX = j;
                    barnY = i;
                }
                else if (row.charAt(j) == 'R')
                {
                    rockX = j;
                    rockY =  i;
                }
                else if (row.charAt(j) == 'L')
                {
                    lakeX = j;
                    lakeY = i;
                }
            }
        }

        int distance = Math.abs(barnX - lakeX) + Math.abs(barnY - lakeY) - 1;
        if (rockX == barnX && rockX == lakeX  && 
        ((barnY < rockY && lakeY > rockY) || (barnY > rockY && lakeY < rockY)))
        {
            distance += 2;
        }

        else if (rockY == barnY && rockY == lakeY && 
        ((barnX < rockX && lakeX > rockX) || (barnX > rockX && lakeX < rockX)))
        {
            distance += 2;
        }
        io.println(distance);
        io.close();
    }
    static class Kattio extends PrintWriter
    {
        private BufferedReader r;
        private StringTokenizer st;

        // standard input
        public Kattio() { this(System.in, System.out); }
        public Kattio(InputStream i, OutputStream o) 
        {
            super(o);
            r = new BufferedReader(new InputStreamReader(i));
        }

        // USACO-style file input
        public Kattio(String problemName) throws IOException
        {
            super(problemName + ".out");
            r = new BufferedReader(new FileReader(problemName + ".in"));
        }

        // returns null if no more input
        public String next()
        {
            try 
            {
                while (st ==  null || !st.hasMoreTokens())
                    st = new StringTokenizer(r.readLine());
                return st.nextToken();
            } catch (Exception e) { }
            return null;
        }
        public int nextInt() { return Integer.parseInt(next()); }
        public double nextDouble() { return Double.parseDouble(next()); }
        public long nextLong() { return Long.parseLong(next()); }
    }
}