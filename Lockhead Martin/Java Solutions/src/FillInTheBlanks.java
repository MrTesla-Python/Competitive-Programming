import java.util.Scanner;
import java.util.HashMap;
public class FillInTheBlanks
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            int positions = in.nextInt();
            int lines = in.nextInt();
            in.nextLine();
            HashMap<String, String> info = new HashMap<String, String>();
            for (int pos = 0; pos < positions; pos++)
            {
                String pos_name = in.nextLine();
                int index = pos_name.indexOf(": ");
                String p = pos_name.substring(0, index);
                String name = pos_name.substring(index+2);
                info.put(p, name);
            }
            for (int line = 0; line < lines; line++)
            {
                String sent = in.nextLine();
                sent = sent.replace("]", "");
                sent = sent.replace("[", "");
                for (String data : info.keySet())
                {
                    if (sent.contains(data))
                    {
                        sent = sent.replace(data, info.get(data));
                    }
                }
                System.out.println(sent);
            }
        }
    }
}