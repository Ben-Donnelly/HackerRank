import java.util.Scanner;

public class ArrayHourglassSum {
    static int calculateHourglassSum(int [][] hourglassArray, int row, int col) {
        return hourglassArray[row][col] +
               hourglassArray[row][col+1] +
               hourglassArray[row][col+2] +
               hourglassArray[row+1][col+1] +
               hourglassArray[row+2][col] +
               hourglassArray[row+2][col+1] +
               hourglassArray[row+2][col+2];
    }
    static int findMax(int [][] hourglassArray) {
        int largestHourglassSum = -54;
        for (int row=0; row<4; row++) {
            for (int col=0; col<4; col++) {
                largestHourglassSum = Math.max(largestHourglassSum, calculateHourglassSum(hourglassArray, row, col));
            }
        }
        return largestHourglassSum;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int [][] hourglassArray = new int[6][6];

        for(int i=0; i<6; i++) {
            for(int j=0; j<6; j++) {
                hourglassArray[i][j] = scan.nextInt();
            }
        }
        scan.close();
        System.out.println(findMax(hourglassArray));
    }
}
