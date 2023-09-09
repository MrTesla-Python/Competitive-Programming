import java.util.Scanner;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Calendar;
public class TimeTroubles {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            String dateTimeString = in.nextLine();
            String[] parts = dateTimeString.split(" ");
            String dateTimePart = parts[0] + " " + parts[1];
            double hoursToAdd = Double.parseDouble(parts[2]);
        
            SimpleDateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy HH:mm");
        
            try {
                Date date = dateFormat.parse(dateTimePart);
            
                Calendar cal = Calendar.getInstance();
                cal.setTime(date);
                cal.add(Calendar.MINUTE, (int) (hoursToAdd * 60 * -1));
            
                Date adjustedDate = cal.getTime();

                String adjustedDateTimeString = dateFormat.format(adjustedDate);
            
                System.out.println(adjustedDateTimeString);
            } catch (ParseException e) {
                e.printStackTrace();
            }
        }
    }
}
