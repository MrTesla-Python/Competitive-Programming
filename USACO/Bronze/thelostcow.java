import java.util.*;
import java.io.*;
public class thelostcow {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("lostcow.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("lostcow.out")));

        StringTokenizer st = new StringTokenizer(r.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        int direction = 1;
        int dist = 1;
        int steps = 0;
        while (true)
        {
            if ((direction == 1 && x <= y && y <= (dist + x)) || (direction == -1 && y <= x && (x - dist <= y)))
            {
                steps += Math.abs(y-x);
                pw.println(steps);
                break;
            }
            else
            {
                steps += (dist*2);
                dist *= 2;
                direction *= -1;
            }
        }
        pw.close();
    }
}
