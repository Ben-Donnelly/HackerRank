import java.util.*;

public class EOF
{
    public static void main(String[] args)
    {

        Scanner scan = new Scanner(System.in);

        int counter=1;

        while(scan.hasNext())
        {
            String s1=scan.nextLine();
            System.out.println(counter + " " + s1);

            counter++;

            if(!scan.hasNext())
            {
                break;
            }
        }
    }
}