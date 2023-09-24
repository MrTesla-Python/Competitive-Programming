import java.util.*;
import java.io.*;
public class wordprocessor {
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("word.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter ("word.out")));

        StringTokenizer st = new StringTokenizer(r.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        String[] words = new String[n];
        st = new StringTokenizer(r.readLine());
        for (int i = 0; i < n; i++)
        {
            words[i] = st.nextToken();
        }
        ArrayList<String> currentString = new ArrayList<String>();
        int currentLineLength = 0;

        for (String word : words)
        {
            if (word.length() + currentLineLength <= k)
            {
                currentString.add(word);
                currentLineLength += word.length();
            }
            else
            {
                pw.println(String.join(" ", currentString));
                currentString.clear();
                currentString.add(word);
                currentLineLength = word.length();
            }
        }
        pw.println(String.join(" ", currentString));

        pw.close();
    }
}
