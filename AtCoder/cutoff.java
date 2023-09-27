import java.util.*;
public class cutoff {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int grade = in.nextInt();
        in.nextLine();

        int[] grades = new int[n-1];
        for (int i = 0; i < n-1; i++)
        {
            grades[i] = in.nextInt();
        } 
        int sum = 0;
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n-1; i++) sum += grades[i];
        Arrays.sort(grades);
        if (grade - (sum - grades[0] - grades[n-2]) < grades[n-2] && grade - (sum - grades[0] - grades[n-2]) > grades[0])
        {
            ans = Math.min(ans, (grade - (sum - grades[0] - grades[n-2])));
        }
        if (grade <= (sum - grades[n-2]))
        {
            ans = Math.min(0, ans);
        }
        if (grade <= (sum - grades[0]))
        {
            ans = Math.min(ans, (grades[n-2]));
        }
        if (ans != Integer.MAX_VALUE) System.out.println(ans);
        else
        {
            System.out.println(-1);
        }
    }
}
