import java.util.*;
import java.io.*;
public class promotioncounting {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("promote.in"));
        PrintWriter pw = new PrintWriter (new BufferedWriter(new FileWriter("promote.out")));

        StringTokenizer st = new StringTokenizer(r.readLine());

        int bronzeBefore = Integer.parseInt(st.nextToken());
        int bronzeAfter = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(r.readLine());
        int silverBefore = Integer.parseInt(st.nextToken());
        int silverAfter = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(r.readLine());
        int goldBefore = Integer.parseInt(st.nextToken());
        int goldAfter = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(r.readLine());
        int platBefore = Integer.parseInt(st.nextToken());
        int platAfter = Integer.parseInt(st.nextToken());

        int promotedSilver = (silverAfter - silverBefore) + (goldAfter - goldBefore) + (platAfter - platBefore);
        pw.println(promotedSilver);

        int promotedGold = (goldAfter - goldBefore) + (platAfter - platBefore);
        pw.println(promotedGold);

        int promotedPlat = (platAfter - platBefore);
        pw.println(promotedPlat);

        pw.close();
    }
}
