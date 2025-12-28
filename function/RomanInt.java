import java.util.Scanner;
public class RomanInt
{
    public static int RomanToInt(String roman) 
    {
        int value[] = new int[r.length()];
        for(int i=0;i<roman.length();i++)
        {
            switch(roman.charAt(i))
            {
                case 'I':
                 value[i]=1;
                 case 'V':
                 value[i]=5;
                 case 'X':
                 value[i]=10;
                 case 'L':
                 value[i]=50;
                 case 'C':
                 value[i]=100;
                 case 'D':
                 value[i]=500;
                 case 'M':
                 value[i]=1000;
                 default:
                 throw new IllegalArgumentException("Invalid Roman Numeral::");

                }
        }
    }
    public static void main(String[] args)
    {
        Scamnner sc = new Scanner(System.in);
        System.out.println("Enter the value in Roman Number");
        String roman = sc.nextInt();
        int result = RomanToInt(roman);
        System.out.println("the integer value is = "+result);
        
    }
}