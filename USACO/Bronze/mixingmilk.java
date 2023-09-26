import java.io.*;
import java.util.*;
public class mixingmilk {
    static int N = 3;
    static int TURN_NUM = 100;
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("mixmilk.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("mixmilk.out")));
        
        int[] capacity = new int[N];
        int[] milk = new int[N];
        for (int i = 0; i < N; i++)
        {
            StringTokenizer st = new StringTokenizer(r.readLine());
            capacity[i] = Integer.parseInt(st.nextToken());
            milk[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < TURN_NUM; i++)
        {
            int bucket1 = i % N;
            int bucket2 = (i + 1) % N;

            int add = Math.min(milk[bucket1], capacity[bucket2] - milk[bucket2]);
            milk[bucket1] -= add;
            milk[bucket2] += add;
        }
        for (int i = 0; i < N; i++) pw.println(milk[i]);
        pw.close();
    }
}
