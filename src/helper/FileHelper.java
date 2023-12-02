package helper;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FileHelper {

    public static List<String> getData(String fileName) throws FileNotFoundException {
        File file = new File(fileName);
        Scanner scanner = new Scanner(file);
        List<String> data = new ArrayList<>();
        while (scanner.hasNextLine()){
            String line = scanner.nextLine();
            if(!"".equals(line)){
                data.add(line);
            }
        }
        return data;
    }
}
