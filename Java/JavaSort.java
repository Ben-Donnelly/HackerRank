import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class CGPACompare implements Comparator<Student> {
    @Override
    public int compare(Student student1, Student student2) {
        if (student1.getStudentCGPA() == student2.getStudentCGPA()) {
            if (student1.getStudentName().compareTo(student2.getStudentName()) == 0) {
                return Integer.compare(student1.getStudentId(), student2.getStudentId());
            }
            return student1.getStudentName().compareTo(student2.getStudentName());
        }
        return Double.compare(student2.getStudentCGPA(), student1.getStudentCGPA());
    }
}


class Student {
    final int studentId;
    final String StudentName;
    final double StudentCGPA;

    Student(int studentId, String StudentName, double StudentCGPA) {
        this.studentId = studentId;
        this.StudentName = StudentName;
        this.StudentCGPA = StudentCGPA;
    }

    public int getStudentId() {
        return studentId;
    }

    public String getStudentName() {
        return StudentName;
    }

    public double getStudentCGPA() {
        return StudentCGPA;
    }
}
public class JavaSort {
    public static void main(String [] args) {
        Scanner scan = new Scanner(System.in);
        int numOfEntries = scan.nextInt();

        Student [] listOfStudents = new Student[numOfEntries];
        Comparator<Student> CGPACompare = new CGPACompare();

        while (numOfEntries-- > 0) {
            int id = scan.nextInt();
            String name = scan.next();
            double CGPA = scan.nextDouble();

            Student newStudent = new Student(id, name, CGPA);
            listOfStudents[numOfEntries] = newStudent;
        }
        Arrays.sort(listOfStudents, CGPACompare);
        for (Student currentStudent : listOfStudents) {
            System.out.println(currentStudent.getStudentName());
        }
    }
}
