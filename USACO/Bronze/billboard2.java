import java.util.*;
import java.io.*;

class Rect {
	int x1, y1, x2, y2;
	int area() { return (y2 - y1) * (x2 - x1); }
}
public class billboard2 {
    public static void main(String[] args) throws IOException
    {

        Rect a = new Rect(), b = new Rect();
        BufferedReader r = new BufferedReader(new FileReader("billboard2.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("billboard2.out")));

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

        int corners = 0;
        if (covered(a.x1, a.y1, b.x1, b.y1, b.x2, b.y2)) corners++;
        if (covered(a.x1, a.y2, b.x1, b.y1, b.x2, b.y2)) corners++;
        if (covered(a.x2, a.y2, b.x1, b.y1, b.x2, b.y2)) corners++;
        if (covered(a.x2, a.y1, b.x1, b.y1, b.x2, b.y2)) corners++;

        int xOverlap = Math.max(0, Math.min(a.x2, b.x2) - Math.max(a.x1, b.x1));
        int yOverlap = Math.max(0, Math.min(a.y2, b.y2) - Math.max(a.y1, b.y1));


        if (corners < 2)
        {
            pw.println(a.area());
        }

        else if (corners == 4)
        {
            pw.println(0);
        }
        else
        {
            pw.println(a.area() - xOverlap * yOverlap);
        }
        pw.close();
    }

    private static boolean covered(int x, int y, int x1, int y1, int x2, int y2)
    {
        return x >= x1 && x <= x2 && y >= y1 && y <= y2;
    }
}
