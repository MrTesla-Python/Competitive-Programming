import java.util.*;
import java.io.*;
public class teleportation {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("teleport.in"));
        PrintWriter pw = new PrintWriter (new BufferedWriter(new FileWriter("teleport.out")));

        StringTokenizer st = new StringTokenizer (r.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        int result = Math.abs(b - a);

        result = Math.min(result, Math.abs(a - x) + Math.abs(y - b));
        result = Math.min(result, Math.abs(a - y) + Math.abs(x - b));

        pw.println(result);
        pw.close();
    }
}
