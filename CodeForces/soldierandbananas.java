import java.util.*;
import java.io.*;
public class soldierandbananas {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pr = new PrintWriter(System.out);

        StringTokenizer st =  new StringTokenizer(r.readLine());

        int k = Integer.parseInt(st.nextToken());
        long n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        long total_cost = w*(w + 1) / 2;
        total_cost *= k;
        System.out.println(Math.max(total_cost - n, 0));

        pr.close();
    }
}
