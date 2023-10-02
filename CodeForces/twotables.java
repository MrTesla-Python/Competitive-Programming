import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;


public class twotables {
    public static void main(String[] args) throws IOException
    {
        Kattio io = new Kattio();
        int t = io.nextInt();
        for (int time = 0; time < t; time++)
        {
            int W = io.nextInt();
            int H = io.nextInt();
            int x1 = io.nextInt();
            int y1 = io.nextInt();
            int x2 = io.nextInt();
            int y2 = io.nextInt();
            int w = io.nextInt();
            int h = io.nextInt();

            int ans = Integer.MAX_VALUE;

            if (W >= w + (x2 - x1))
            {
                ans = Math.min(ans, Math.min(Math.max(0, (w-x1)), Math.max(0, (x2 - (W-w)))));
            }
            if (H >= h + (y2 - y1))
            {
                ans = Math.min(ans, Math.min(Math.max(0, (h-y1)), Math.max(0, (y2 - (H-h)))));
            }
            if (ans == Integer.MAX_VALUE) io.println(-1);
            else io.println(ans);
        }
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

	static class Rect {
		public long x1, y1, x2, y2;
		public Rect(long a, long b, long c, long d) {
			x1 = a;
			y1 = b;
			x2 = c;
			y2 = d;
		}

		public long area() { return (x2 - x1) * (y2 - y1); }
	}
}
