import java.util.*;
import java.io.*;
public class bovinegenomics
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("cownomics.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cownomics.out")));
        
        StringTokenizer st = new StringTokenizer(r.readLine());
        int ncows = Integer.parseInt(st.nextToken());
        int length = Integer.parseInt(st.nextToken());

        String[] badcows = new String[ncows];
        String[] goodcows = new String[ncows];
        for (int i = 0; i < ncows; i++) 
        {
            badcows[i] = r.readLine();
        }
        for (int i = 0; i < ncows; i++)
        {
            goodcows[i] = r.readLine();
        }
        int count = 0;
        Set<String> check = new HashSet<String>();
        for (int i = 0; i < length; i++)
        {
            boolean checks = true;
            for (int j = 0; j < ncows; j++)
            {
                check.add(Character.toString(badcows[j].charAt(i)));
            }
            for (int j = 0; j < ncows; j++)
            {
                if (check.contains(Character.toString(goodcows[j].charAt(i))))
                {
                    checks = false;
                    break;
                }

            }
            if (checks) count++;
            check.clear();
        }
        pw.println(count);
        pw.close();
    }
}