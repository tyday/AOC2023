package Day01;

import helper.FileHelper;

import java.io.FileNotFoundException;
import java.util.List;

public class Day01 {
    public static void main(String[] args) throws FileNotFoundException {
        List<String> data = FileHelper.getData("C:\\LocalProgramming\\AOC2023\\src\\Day01\\data.txt");
        System.out.println(data);
        int total = 0;
        for (String line :
                data) {
            int firstDigit = getFirstDigit(line);
            int secondDigit = getSecondDigit(line);
            int result = firstDigit * 10 + secondDigit;
            System.out.println(result);
            total += result;

        }
        System.out.println("Total for part one is: " + total);
    }

    private static int getSecondDigit(String line) {
        for (int i = line.length() - 1; i > -1; i--) {
            Character c = line.charAt(i);
            if (Character.isDigit(c)){
                return Character.getNumericValue(c);
            }
        }
        return 0;
    }

    private static int getFirstDigit(String line) {
        for (int i = 0; i < line.length(); i++) {
            Character c = line.charAt(i);
            if (Character.isDigit(c)){
                return Character.getNumericValue(c);
            }
        }
        return 0;
    }
}
