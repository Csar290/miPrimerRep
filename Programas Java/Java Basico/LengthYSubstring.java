import java.util.Scanner;

public class LengthYSubstring {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String cadena = "", cadena_nueva = "";
        int longitud = 0, inicio = 0, fin = 0;

        System.out.print("Introduce una cadena de caracteres: ");
        cadena = entrada.nextLine();
        longitud = cadena.length();
        System.out.println("La cadena de caracteres " + cadena + " tiene " + longitud + " caracteres");

        System.out.println("¿Desde que caracter deseas obtener la nueva cadena?");
        inicio = entrada.nextInt();
        System.out.println("¿Hasta que caracter deseas obtener la nueva cadena?");
        fin = entrada.nextInt();
        cadena_nueva = cadena.substring(inicio, fin);
        System.out.print("La nueva cadena es: " + cadena_nueva);
    }
}