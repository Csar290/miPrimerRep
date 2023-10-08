import java.util.Scanner;

public class EjercicioPractico7 {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int filas = 0, columnas = 0, contador = 1;

        System.out.print("¿Cuantas filas quieres que tenga la matriz?: ");
        filas = input.nextInt();

        System.out.print("¿Cuantas columnas quieres que tenga la matriz?: ");
        columnas = input.nextInt();

        int matriz[][] = new int [filas][columnas];

        for (int j = 0; j < columnas; j++) {
            for (int i = 0; i < filas; i++) {
                matriz[j][i] = contador;
                System.out.print("[" + matriz[j][i] + "]");
                contador++;
            }
            System.out.println("");
        }
    }
}
