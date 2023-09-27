import java.util.*;
import java.io.*;
public class circularbarn {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("cbarn.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cbarn.out")));

        int n = Integer.parseInt(r.readLine());
        int[] doors = new int[n];
        int totalcows = 0;
        for (int i = 0; i < n; i++)
        {
            int door = Integer.parseInt(r.readLine());
            doors[i] = door;
            totalcows += door;
        }

        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++)
        {
            int currdist = 0;
            int cowsleft = totalcows;
            for (int j = 0; j < n; j++)
            {
                cowsleft -= doors[(i + j) % n];
                currdist += doors[(i+j) % n] * j;
            }
            minDist = Math.min(minDist, currdist);
        }
        pw.println(minDist);
        pw.close();
    }
}
