import java.util.Scanner;
public class Autocorrect {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            int dict_count = in.nextInt();
            int word_count = in.nextInt();
            in.nextLine();
            String[] dict = new String[dict_count];
            for (int word = 0; word < dict_count; word++)
            {
                dict[word] = in.nextLine();
            }
            for (int i = 0; i < word_count; i++)
            {
                String ans = closest(dict, in.nextLine());
                System.out.println(ans);
            }
        }
        in.close();
    }
    public static String closest(String[] dict, String word)
    {
        int less = Integer.MAX_VALUE;
        String value = null;
        for (int i = 0; i < dict.length; i++)
        {
            int count = 0;
            if (word.length() == dict[i].length())
            {
                for (int j = 0; j < word.length(); j++)
                {
                    if (word.charAt(j) != dict[i].charAt(j));
                    {
                        count++;
                    }
                }
                if (count < less)
                {
                    less = count;
                    value = dict[i];
                }
            }

        }
        return value;
    }
}
