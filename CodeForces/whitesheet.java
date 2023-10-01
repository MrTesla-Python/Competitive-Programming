import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;


public class whitesheet {
    public static void main(String[] args) throws IOException
    {
        Kattio io = new Kattio();
        Rect A =
		    new Rect(io.nextLong(), io.nextLong(), io.nextLong(), io.nextLong());
		Rect B =
		    new Rect(io.nextLong(), io.nextLong(), io.nextLong(), io.nextLong());
		Rect C =
		    new Rect(io.nextLong(), io.nextLong(), io.nextLong(), io.nextLong());

		long intersect1 = calcintersect(A, B);
		long intersect2 = calcintersect(A, C);
		Rect wb1 = new Rect(Math.max(A.x1, B.x1), Math.max(A.y1, B.y1), Math.min(A.x2, B.x2), Math.min(A.y2, B.y2));
		Rect wb2 = new Rect(Math.max(A.x1, C.x1), Math.max(A.y1, C.y1), Math.min(A.x2, C.x2), Math.min(A.y2, C.y2));
		long intersect3 = calcintersect(wb1, wb2);
        long ans = intersect1 + intersect2 - intersect3;
        if (A.area() > ans) io.println("YES");
        else io.println("NO");
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

    public static long calcintersect(Rect a, Rect b)
    {
        long xoverlap = Math.max(0, Math.min(a.x2, b.x2) - Math.max(a.x1, b.x1));
        long yoverlap = Math.max(0, Math.min(a.y2, b.y2) - Math.max(a.y1, b.y1));

        return xoverlap*yoverlap;
    }

    public static Rect change(Rect a, Rect b)
    {
        if (b.x1 < a.x1) b.x1 = a.x1;
        if (b.x2 > a.x2) b.x2 = a.x2;
        if (b.y1 < a.y1) b.y1 = a.y1;
        if (b.y2 > a.y2) b.y2 = a.y2;
		return b;
    }

}
