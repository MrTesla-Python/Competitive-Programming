import java.io.*;
import java.util.*;
public class fencepainting {
    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new FileReader("paint.in"));
        PrintWriter pw = new PrintWriter (new BufferedWriter(new FileWriter("paint.out")));
        StringTokenizer st = new StringTokenizer(r.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(r.readLine());

        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        int total = (b - a) + (d - c);
        int intersection = Math.max(Math.min(b, d) - Math.max(a, c), 0);
        int union = total - intersection;

        pw.println(union);
        pw.close();
    }
}
