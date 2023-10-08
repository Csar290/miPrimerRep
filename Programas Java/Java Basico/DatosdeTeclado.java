import java.util.Scanner;

public class DatosdeTeclado {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String nombre = "";
        int num1 = 0, num2 = 0, resultado = 0;

        System.out.println("¿Cual es tu nombre?");
        nombre = entrada.nextLine();

        System.out.println("Hola " + nombre + " dame el primer valor para sumar");
        num1 = entrada.nextInt();

        System.out.println("Ahora dame el segundo valor");
        num2 = entrada.nextInt();

        resultado = num1 + num2;

        System.out.println(nombre + " el resultado de tu suma es: " + resultado);
    }
}
