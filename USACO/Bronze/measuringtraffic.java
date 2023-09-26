import java.util.*;
import java.io.*;
public class measuringtraffic {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("traffic.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("traffic.out")));

        int n = Integer.parseInt(r.readLine());
        int[] left = new int[n];
        int[] right = new int[n];
        String[] string = new String[n];

        for (int i = 0; i < n; i++)
        {
            StringTokenizer st = new StringTokenizer(r.readLine());
            string[i] = st.nextToken();
            left[i] = Integer.parseInt(st.nextToken());
            right[i] = Integer.parseInt(st.nextToken());
        }

        int a = -9999999;
        int b = 9999999;
        for (int i = n - 1; i >= 0; i--)
        {
            if (string[i].equals("none"))
            {
                a = Math.max(a, left[i]);
                b = Math.min(b, right[i]);
            }
            else if (string[i].equals("off"))
            {
                a += left[i];
                b += right[i];
            }
            else if (string[i].equals("on"))
            {
                a -= right[i];
                b -= left[i];
                a = Math.max(a, 0);
                b = Math.max(b, 0);
            }
        }
        pw.println(a + " " + b);

        a = -9999999;
        b = 9999999;
        for (int i = 0; i < n; i++)
        {
            if (string[i].equals("none"))
            {
                a = Math.max(a, left[i]);
                b = Math.min(b, right[i]);
            }
            else if (string[i].equals("off"))
            {
                b -= left[i];
                a -= right[i];
                a = Math.max(a, 0);
                b = Math.max(b, 0);
            }
            else if (string[i].equals("on"))
            {
                a += left[i];
                b += right[i];
            }
        }
        pw.println(a + " " + b);
        pw.close();
    }
}
