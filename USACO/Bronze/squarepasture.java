import java.util.*;
import java.io.*;
public class squarepasture
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("square.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("square.out")));

        StringTokenizer st = new StringTokenizer(r.readLine());
        int x1 = Integer.parseInt(st.nextToken());
        int y1 = Integer.parseInt(st.nextToken());
        int x2 = Integer.parseInt(st.nextToken());
        int y2 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(r.readLine());

        int x3 = Integer.parseInt(st.nextToken());
        int y3 = Integer.parseInt(st.nextToken());
        int x4 = Integer.parseInt(st.nextToken());
        int y4 = Integer.parseInt(st.nextToken());

        int left = Math.min(x1, x3);
        int right = Math.max(x2, x4);
        int bottom = Math.min(y1, y3);
        int top = Math.max(y2, y4);

        int width = right-left;
        int height = top-bottom;
        pw.println(Math.max(width, height) * Math.max(width, height));
        pw.close();
    }
}