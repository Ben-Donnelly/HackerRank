import java.util.HashMap;
import java.util.Scanner;

class PhoneBook {
    private final HashMap<String, String> phoneBook;

    public PhoneBook() {
        phoneBook = new HashMap<>();
    }

    public void addToPhonebook(String name, String number) {
        phoneBook.put(name, number);
    }

    public boolean checkIfNameInPhoneBook(String name) {
        return phoneBook.containsKey(name);
    }

    public String getNumber(String name) {
        return phoneBook.get(name);
    }
}

public class JavaPhoneBook {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        PhoneBook phoneBook = new PhoneBook();

        int numOfEntries = Integer.parseInt(scan.nextLine());

        while (numOfEntries-- > 0) {
            String name = scan.nextLine();
            String number = scan.nextLine();

            phoneBook.addToPhonebook(name, number);
        }

        while (scan.hasNext()) {
            String nameToLookup = scan.nextLine();

            if (phoneBook.checkIfNameInPhoneBook(nameToLookup)) {
                String number = phoneBook.getNumber(nameToLookup);
                System.out.format("%s=%s%n", nameToLookup, number);
            } else {
                System.out.println("Not found");
            }
        }
        scan.close();
    }
}
