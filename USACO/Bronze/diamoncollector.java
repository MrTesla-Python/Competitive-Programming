import java.util.*;
import java.io.*;
public class diamoncollector {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("diamond.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("diamond.out")));

        StringTokenizer st = new StringTokenizer(r.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] cows = new int[N];
        for (int i = 0; i < N; i++)
        {
            cows[i] = Integer.parseInt(r.readLine());
        }
        int ans = 0;
        for (int i : cows)
        {
            int points = 0;
            for (int j : cows)
            {
                if (i <= j && i + K >= j)
                {
                    points++;
                }
            }
            ans = Math.max(ans, points);
        }
        pw.println(ans);
        pw.close();
    }
}
