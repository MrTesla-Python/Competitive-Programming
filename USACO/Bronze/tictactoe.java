import java.util.*;
import java.io.*;
public class tictactoe {
    static char [][] board = new char[3][3];

    static int cow_wins(char ch) {
		// Check diagonals
		if (board[0][0] == ch && board[1][1] == ch && board[2][2] == ch) return 1;
		if (board[0][2] == ch && board[1][1] == ch && board[2][0] == ch) return 1;

		// Check rows and columns
		for (int i = 0; i < 3; i++) {
			if (board[0][i] == ch && board[1][i] == ch && board[2][i] == ch) return 1;
			if (board[i][0] == ch && board[i][1] == ch && board[i][2] == ch) return 1;
		}

		return 0;
	}

    static boolean check(char ch1, char ch2, char a, char b, char c)
    {
        if (ch1 != a && ch1 != b && ch1 != c) return false;
        if (ch2 != a && ch2 != b && ch2 != c) return false;

        if (a != ch1 && a != ch2) return false;
        if (b != ch1 && b != ch2) return false;
        if (c != ch1 && c != ch2) return false;

        return true;
    }

    static int two_wins(char ch1, char ch2)
    {
        if (check(ch1, ch2, board[0][0], board[1][1], board[2][2])) return 1;
        if (check(ch1, ch2, board[0][2], board[1][1], board[2][0])) return 1;

        for (int i = 0; i < 3; i++)
        {
            if (check(ch1, ch2, board[0][i], board[1][i], board[2][i])) return 1;
            if (check(ch1, ch2, board[i][0], board[i][1], board[i][2])) return 1;
        }
        return 0;
    }
    public static void main(String[] args) throws IOException
    {
        BufferedReader r = new BufferedReader(new FileReader("tttt.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("tttt.out")));

        for (int row = 0; row < 3; row++)
        {
            String line = r.readLine();
            board[row] = line.toCharArray();
        }
        int singleplayer = 0;
        int doubleplayer = 0;

        for (char ch = 'A'; ch <= 'Z'; ch++) { singleplayer += cow_wins(ch);}

        for (char ch1 = 'A'; ch1 <= 'Z'; ch1++)
        {
            for (char ch2 = (char) (ch1 + 1); ch2 <= 'Z'; ch2++) 
            { 
                doubleplayer += two_wins(ch1, ch2);
            }
        }
        
        pw.println(singleplayer);
        pw.println(doubleplayer);
        pw.close();
    }
}
