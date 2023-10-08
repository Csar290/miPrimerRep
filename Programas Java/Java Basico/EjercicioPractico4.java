import java.util.Scanner;

public class EjercicioPractico4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String nombre1 = "", nombre2 = "";

        System.out.println("Por favor ingresa el primer nombre");
        nombre1 = input.nextLine();

        System.out.println("Por favor ingresa el segundo nombre");
        nombre2 = input.nextLine();

        if (nombre1.equalsIgnoreCase(nombre2)) {System.out.println("Los nombre son iguales");}
        else{System.out.println("Los nombre no son iguales");}
    }
}
