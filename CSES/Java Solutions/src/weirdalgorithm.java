import java.io.*;
public class weirdalgorithm {
    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        long a = Long.parseLong(r.readLine());
        while (a != 1)
        {
            pw.print(a + " ");
            if (a % 2 == 0) a /= 2;
            else a = 3 * a + 1;

        }
        pw.println(a);
        pw.close();
        
    }
}
