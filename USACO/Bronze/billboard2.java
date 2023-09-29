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
        a.y2 = Integer.parseInt(st.nextToken());
        a.x2 = Integer.parseInt(st.nextToken());
        a.y2 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(r.readLine());
        b.x1 = Integer.parseInt(st.nextToken());
        b.y1 = Integer.parseInt(st.nextToken());
        b.x2 = Integer.parseInt(st.nextToken());
        b.y2 = Integer.parseInt(st.nextToken());

        int xOverlap = Math.max(0, Math.min(a.x2, b.x2) - Math.max(a.x1, b.x1));
        int yOverlap = Math.max(0, Math.min(a.y2, b.y2) - Math.max(a.y1, b.y1));
        
    }
}
