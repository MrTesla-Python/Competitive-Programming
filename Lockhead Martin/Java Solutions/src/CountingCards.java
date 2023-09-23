import java.util.HashMap;
import java.util.Scanner;
public class CountingCards {

    public static int calcPoints(String[] hand)
    {
        HashMap<String, Integer> points1 = new HashMap<String, Integer>();
        HashMap<String, Integer> points2 = new HashMap<String, Integer>();
        points1.put("2", 2);
        points1.put("3", 3);
        points1.put("4", 4);
        points1.put("5", 5);
        points1.put("6",6);
        points1.put("7", 7);
        points1.put("8", 8);
        points1.put("9", 9);
        points1.put("10", 10);
        points1.put("JACK", 10);
        points1.put("QUEEN", 10);
        points1.put("KING", 10);
        points1.put("ACE", 11);

        points2.put("2", 2);
        points2.put("3", 3);
        points2.put("4", 4);
        points2.put("5", 5);
        points2.put("6",6);
        points2.put("7", 7);
        points2.put("8", 8);
        points2.put("9", 9);
        points2.put("10", 10);
        points2.put("JACK", 10);
        points2.put("QUEEN", 10);
        points2.put("KING", 10);
        points2.put("ACE", 1);
        int pointval1 = 0;
        int pointval2 = 0;
        for (String card : points1.keySet())
        {
            for (int i = 0; i < hand.length; i++)
            {
                if (hand[i].contains(card))
                {
                    pointval1 += points1.get(card);
                }
            }
        }
        for (String card : points2.keySet())
        {
            for (int i = 0; i < hand.length; i++)
            {
                if (hand[i].contains(card))
                {
                    pointval2 += points2.get(card);
                }
            }
        }
        if (pointval1 > pointval2 && pointval1 < 22)
        {
            return pointval1;
        }
        else
        {
            return pointval2;
        }
    }
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            String[] playerHand = in.nextLine().split(" ");
            String[] dealerHand = in.nextLine().split(" ");
            int playerScore = calcPoints(playerHand);
            int dealerScore = calcPoints(dealerHand);
            if ((playerScore > dealerScore && playerScore <= 21) || (playerScore < dealerScore && dealerScore > 21))
            {
                System.out.printf("Player Score: %d Dealer Score: %d Player Wins!%n", playerScore, dealerScore);
            }
            else if ((playerScore < dealerScore && dealerScore <= 21) || (dealerScore < playerScore && playerScore > 21))
            {
                System.out.printf("Player Score: %d Dealer Score: %d Dealer Wins!%n", playerScore, dealerScore);
            }
            else
            {
                System.out.printf("Player Score: %d Dealer Score: %d Tie!%n", playerScore, dealerScore);
            }
        }
    }
}
