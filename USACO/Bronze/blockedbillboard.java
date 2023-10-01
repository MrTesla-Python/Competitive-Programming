import java.util.*;
import java.io.*;
import java.awt.Rectangle;

class Rect {
        int x1, y1, x2, y2;
        int area() { return (y2 - y1) * (x2 - x1); }
    }
public class blockedbillboard {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("billboard.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("billboard.out")));

        
        Rect a = new Rect(), b = new Rect(), t = new Rect();
        StringTokenizer st = new StringTokenizer(r.readLine());
        a.x1 = Integer.parseInt(st.nextToken());
		a.y1 = Integer.parseInt(st.nextToken());
		a.x2 = Integer.parseInt(st.nextToken());
		a.y2 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(r.readLine());
		b.x1 = Integer.parseInt(st.nextToken());
		b.y1 = Integer.parseInt(st.nextToken());
		b.x2 = Integer.parseInt(st.nextToken());
		b.y2 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(r.readLine());
		t.x1 = Integer.parseInt(st.nextToken());
		t.y1 = Integer.parseInt(st.nextToken());
		t.x2 = Integer.parseInt(st.nextToken());
		t.y2 = Integer.parseInt(st.nextToken());

        pw.println(a.area() + b.area() - calcintersect(a, t) - calcintersect(t, b));
        pw.close();
    }

    public static int calcintersect(Rect a, Rect b)
    {
        int xoverlap = Math.max(0, Math.min(a.x2, b.x2) - Math.max(a.x1, b.x1));
        int yoverlap = Math.max(0, Math.min(a.y2, b.y2) - Math.max(a.y1, b.y1));

        return xoverlap*yoverlap;
    }
}
