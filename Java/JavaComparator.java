import java.util.Comparator;
import java.util.Scanner;
import java.util.Arrays;

class Player{
    final String name;
    final int score;

    Player(String name, int score){
        this.name = name;
        this.score = score;
    }
}

class PlayerScoreComparison implements Comparator<Player> {
    @Override
    public int compare(Player player1, Player player2) {
        if (player2.score == player1.score) {
            return player1.name.compareTo(player2.name);
        }
        return Integer.compare(player2.score, player1.score);
    }
}

public class JavaComparator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int numOfEntries = scan.nextInt();

        Player[] playerList = new Player[numOfEntries];
        PlayerScoreComparison playerScoreComparison = new PlayerScoreComparison();

        while (numOfEntries-- > 0){
            String playerName = scan.next();
            int playerScore = scan.nextInt();

            // Yes, I'm filling up the array backwards. Why? fun.
            playerList[numOfEntries] = new Player(playerName, playerScore);
        }
        scan.close();

        Arrays.sort(playerList, playerScoreComparison);
        for (Player currentPlayer : playerList){
            System.out.format("%s %s%n", currentPlayer.name, currentPlayer.score);
        }
    }
}

