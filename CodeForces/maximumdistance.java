import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class maximumdistance {
    public static void main(String[] args)
    {
        Kattio io = new Kattio();
        int n = io.nextInt();

        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) x[i] = io.nextInt();
        for (int i = 0; i < n; i++) y[i] = io.nextInt();

        int maxDist = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                int dx = x[i] - x[j];
                int dy = y[i] - y[j];
                int square = (int) (Math.pow(dx, 2) + Math.pow(dy, 2));
                maxDist = Math.max(maxDist, square);
            }
        }
        io.println(maxDist);
        io.close();
    }
    static class Kattio extends PrintWriter {
		private BufferedReader r;
		private StringTokenizer st;
		// standard input
		public Kattio() { this(System.in, System.out); }
		public Kattio(InputStream i, OutputStream o) {
			super(o);
			r = new BufferedReader(new InputStreamReader(i));
		}
		// USACO-style file input
		public Kattio(String problemName) throws IOException {
			super(problemName + ".out");
			r = new BufferedReader(new FileReader(problemName + ".in"));
		}
		// returns null if no more input
		public String next() {
			try {
				while (st == null || !st.hasMoreTokens())
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

