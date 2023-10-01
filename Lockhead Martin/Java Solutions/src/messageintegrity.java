import java.util.*;
public class messageintegrity {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            String[] string = in.nextLine().split("");
            int[] code = new int[string.length];
            int[] compare = {1, 0, 1, 1};

            for (int i = 0; i < string.length; i++) code[i] = Integer.parseInt(string[i]);

            int index = 0;
            while (index < string.length-4)
            {
            int count = 0;
            for (int j = 0; j < 4; j++)
            {
                if (code[j+index] != compare[j])
                {
                    code[j+index] = 1;
                    if (count == 0)
                    {
                        index += j;
                        count++;
                    }
                }
            }
            if (count == 0) index += 4;
        }
        boolean check = true;
        for (int i = 0; i < code.length; i++) 
        {
            if (code[i] == 1) 
            {
                check = false;
                break;
            }
        }
        if (check) System.out.println("ok");
        else System.out.println("corrupt");
        }
    }
}
