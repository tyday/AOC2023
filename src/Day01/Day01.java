package Day01;

import helper.FileHelper;

import java.io.FileNotFoundException;
import java.util.List;
import java.util.Map;

public class Day01 {
    public static void main(String[] args) throws FileNotFoundException {
        List<String> data = FileHelper.getData("C:\\LocalProgramming\\AOC2023\\src\\Day01\\data.txt");
        System.out.println(data);
        int total = 0;
        for (String line :
                data) {
            int firstDigit = getFirstDigit(line, false);
            int secondDigit = getSecondDigit(line, false);
            int result = firstDigit * 10 + secondDigit;
//            System.out.println(result);
            total += result;

        }
        System.out.println("Total for part one is: " + total);

        // Part two
        total = 0;
//        data = FileHelper.getData("C:\\LocalProgramming\\AOC2023\\src\\Day01\\testdata2.txt");
        for (String line :
                data) {
            int firstDigit = getFirstDigit(line, true);
            int secondDigit = getSecondDigit(line, true);
            int result = firstDigit * 10 + secondDigit;
//            System.out.println(result);
            total += result;

        }
        System.out.println("Total for part two is: " + total);
    }

    private static int getSecondDigit(String line, boolean partTwo) {
        String val = "";
        for (int i = line.length() - 1; i > -1; i--) {
            Character c = line.charAt(i);
            if (Character.isDigit(c)){
                return Character.getNumericValue(c);
            }
            if(partTwo){
                val = Character.toLowerCase(c) + val;
                for (String numb :
                        numbers) {
                    if(val.contains(numb)){
                        return values.valueOf(numb).ordinal();
                    }
                }
            }
        }
        return 0;
    }

    private static int getFirstDigit(String line, boolean partTwo) {
        String val = "";
        for (int i = 0; i < line.length(); i++) {
            Character c = line.charAt(i);
            if (Character.isDigit(c)){
                return Character.getNumericValue(c);
            }
            if(partTwo){
                val = val + Character.toLowerCase(c);
                for (String numb :
                        numbers) {
                    if(val.contains(numb)){
                        return values.valueOf(numb).ordinal();
                    }
                }
            }
        }
        return 0;
    }

    static List<String> numbers = List.of(
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "zero"
    );

    static enum values{
        zero,
        one,
        two,
        three,
        four,
        five,
        six,
        seven,
        eight,
        nine
    }
}
