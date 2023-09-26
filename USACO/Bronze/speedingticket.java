import java.util.*;
import java.io.*;
public class speedingticket {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("speeding.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("speeding.out")));

        StringTokenizer st = new StringTokenizer(r.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int [][] should = new int[n][2];
        int [][] actual = new int[m][2];

        for (int i = 0; i < n; i++)
        {
            st = new StringTokenizer(r.readLine());
            should[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }

        for (int i = 0; i < n; i++)
        {
            st = new StringTokenizer(r.readLine());
            actual[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }

        int [] compares1 = new int[100];
        int [] compares2 = new int [100];
        for (int[] speeds : should)
        {
            for (int i = 0; i < speeds[0]; i++)
            {
                compares1[i] = speeds[1];
            }
        }

        for (int[] speeds : actual)
        {
            for (int i = 0; i < speeds[0]; i++)
            {
                compares2[i] = speeds[1];
            }
        }

        int max = 0;
        for (int i = 0; i < 100; i++)
        {
            max = Math.max((compares2[i] - compares1[i]), max);
        }
        pw.println(max);
        pw.close();
        
    }
}
