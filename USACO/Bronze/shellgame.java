import java.io.*;
import java.util.*;
public class shellgame
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("shell.in"));        
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("shell.out")));
        
        int times = Integer.parseInt(r.readLine());
        int[] count = new int[3];
        int[] shells = new int[] {0, 1, 2};
        int maxPoints = 0;
        for (int i = 0; i < times; i++)
        {
            StringTokenizer st = new StringTokenizer(r.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int g = Integer.parseInt(st.nextToken()) - 1;
            
            int temp = shells[b];
            shells[b] = shells[a];
            shells[a] = temp;

            count[shells[g]] += 1;

            maxPoints = Math.max(maxPoints, count[shells[g]]);
        }

        pw.println(maxPoints);
        pw.close();
    }
}