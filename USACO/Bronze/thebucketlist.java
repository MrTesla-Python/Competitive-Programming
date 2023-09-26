import java.util.*;
import java.io.*;
public class thebucketlist {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("blist.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("blist.out")));

        int max = 1000;
        int n = Integer.parseInt(r.readLine());
        int[] milks = new int[max];
        for (int i = 0; i < n; i++)
        {
            StringTokenizer st = new StringTokenizer(r.readLine());
            int start = Integer.parseInt(st.nextToken()) - 1;
            int end = Integer.parseInt(st.nextToken()) - 1;
            int milk = Integer.parseInt(st.nextToken());

            milks[start] += milk;
            milks[end] -= milk;

        }
        int jugs = 0;
        int curr = 0;
        for (int i = 0; i < max; i++)
        {
            curr += milks[i];
            jugs = Math.max(jugs, curr);
        }
        pw.println(jugs);
        pw.close();
    }
}
