import java.util.Scanner;

public class EjercicioPractico6 {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int longitud = 0;

        System.out.print("¿Cuantas posiciones quieres que tenga el vector?: ");
        longitud = input.nextInt();

        int vector[] = new int[longitud];

        for (int i = 0; i < longitud; i++) {
            System.out.print("Proporcioname el valor para la posicion " + i + ": ");
            vector[i] = input.nextInt();
        } for (int i = 0; i < vector.length; i++) {
            System.out.print("[" + vector[i] + "]");
        }
    }
}
