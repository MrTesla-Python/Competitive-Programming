import java.util.*;
import java.io.*;
public class soldierandbananas {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pr = new PrintWriter(System.out);

        StringTokenizer st =  new StringTokenizer(r.readLine());

        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        int total_cost = 0;
        for (int i = 1; i <= w; i++) total_cost += (i*k);
        System.out.println(total_cost - n);
    }
}
