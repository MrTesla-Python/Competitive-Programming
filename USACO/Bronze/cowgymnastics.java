import java.util.*;
import java.io.*;
public class cowgymnastics {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("gymnastics.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("gymnastics.out")));
        StringTokenizer st = new StringTokenizer(r.readLine());

        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[][] ranks = new int[K][N];
        for (int i = 0; i < K; i++)
        {
            st = new StringTokenizer(r.readLine());
            for (int j = 0; j < N; j++)
            {
                ranks[i][j] = Integer.parseInt(st.nextToken()) - 1;
            }
        }
        int betterPairs = 0;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (i == j) continue;

                boolean pair = true;
                for (int[] s : ranks)
                {
                    if (index(s, i) < index(s, j))
                    {
                        pair = false;
                        break;
                    }
                }
                if (pair) betterPairs++;
            }
        }
        pw.println(betterPairs);
        pw.close();
    }
    public static int index(int[] arr, int n)
    {
        for (int i = 0; i < arr.length; i++)
        {
            if (arr[i] == n) return i;
        }
        return -1;
    } 
}
