import java.util.*;
import java.io.*;
public class blockgame {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("blocks.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("blocks.out")));

        int times = Integer.parseInt(r.readLine());
        String[][] words = new String[times][]; 
        int[] letters = new int[26];
        
        for (int i = 0; i < times; i++)
        {
            StringTokenizer st = new StringTokenizer(r.readLine());
            words[i] = new String[] {st.nextToken(), st.nextToken()};
        }

        for (String[] word : words)
        {
            int[] count1 = (count(word[0]));
            int[] count2 = (count(word[1]));
            for (int i = 0; i < 26; i++)
            {
                letters[i] += Math.max(count1[i], count2[i]);
            }
        }
        for (int i = 0; i < 26; i++)
        {
            pw.println(letters[i]);
        }
        pw.close();
    }
    public static int[] count(String word)
    {
        int[] count = new int[26];
        for (int i = 0; i < word.length(); i++)
        {
            count[word.charAt(i) - 'a']+=1;
        }
        return count;
    }
}
