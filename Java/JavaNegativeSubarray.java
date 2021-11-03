import java.util.Scanner;

public class JavaNegativeSubarray {
    static int getAllSubarrays(int [] a) {
        int runningSum;
        int countOfNegativeSubArrays = 0;

        for (int i=0; i<a.length; i++) {
            runningSum = 0;
            for (int j=i; j<a.length; j++) {
                runningSum += a[j];
                if (runningSum < 0) {
                    countOfNegativeSubArrays++;
                }
            }
        }
        return countOfNegativeSubArrays;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int arraySize = scan.nextInt();
        int [] a = new int[arraySize];

        for (int i=0; i<arraySize; i++) {
            a[i] = scan.nextInt();
        }
        System.out.println(getAllSubarrays(a));
    }
}
