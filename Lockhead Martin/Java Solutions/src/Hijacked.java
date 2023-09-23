import java.util.Scanner;
public class Hijacked
{
    public static String reverse(String s)
    {
        String reversedString = "";
        for (int i =  s.length() - 1; i >= 0; i--)
        {
            reversedString += s.charAt(i);
        }
        return reversedString;
    }

    public static String printAns(String beg, String sents)
    {
        String ans = "";
        for (int i = 0; i < sents.length(); i++)
            {
                if (beg.indexOf(sents.charAt(i)) > -1)
                {
                    ans += sents.charAt(i);
                    i++;
                }
                else
                {
                    ans += sents.charAt(i);
                }
            }
        return ans;
    }
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            String sents = "";
            String beg = "";
            int length = in.nextInt();
            in.nextLine();
            String sent = in.nextLine(); 
            for (int i = 0; i < sent.length(); i++)
            {
                if (i + 3 < sent.length())
                {
                    beg = sent.substring(i, i+3);
                    if (sent.indexOf(reverse(beg)) >= 0 && sent.indexOf(reverse(beg)) > i+2)
                    {
                        sents = sent.substring(i+3, sent.indexOf(reverse(beg)));
                        i = sent.indexOf(reverse(beg)) + 2;
                        System.out.println(printAns(beg, sents));
                    }
                }
            }
        }
    }
}