import java.util.Scanner;
import java.util.Set;
import java.util.Stack;

public class JavaStack {
    public static boolean isBalanced(String s1) {
        Set<Character> openingBrackets = Set.of('(', '{', '[');
        Stack<Character> bracketStack = new Stack<>();

        for (Character currentCharacter : s1.toCharArray()) {
            if (openingBrackets.contains(currentCharacter)) {
                bracketStack.push(currentCharacter);
            } else {
                if (bracketStack.empty()) {
                    return false;
                }
                switch (currentCharacter) {
                    case ')':
                        if (bracketStack.pop() != '(') {
                            return false;
                        }
                        break;

                    case '}':
                        if (bracketStack.pop() != '{') {
                            return false;
                        }
                        break;

                    case ']':
                        if (bracketStack.pop() != '[') {
                            return false;
                        }
                        break;
                }
            }
        }
        return bracketStack.empty();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        while (scan.hasNext()) {
            System.out.println(isBalanced(scan.nextLine()));
        }
    }
}
