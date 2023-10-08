import java.util.Scanner;

public class Ologicosyrelacionales {
    public static void main(String[] args){
        //Declaramos las variables
        Scanner in = new Scanner(System.in);
        String nombre = "";
        int clave = 0, antiguedad = 0;

        //Bienvenida
        System.out.println("Bienvenido al sistema vacional de Pepsi Cola");

        //Le pedimos su nombre
        System.out.println("¿Cúal es tu nombre?");
        nombre = in.nextLine();

        //Le pedimos la cantidad de años que lleva trabajando 
        System.out.println("¿Cuantos años lleva en la empresa?");
        antiguedad = in.nextInt();

        //Le pedimos su clave
        System.out.println("¿Cúal es su número de clave?");
        clave = in.nextInt();

        // Atencion al cliente
        if (clave == 1) {
            // 1 año de servicio
            if (antiguedad == 1) {
                System.out.println(nombre + " usted tiene derecho a 6 dias de vacaciones.");

            // De 2 a 6 años de servicio 
            } else if (antiguedad >= 2 && antiguedad <= 6) {
                System.out.println(nombre + " usted tiene derecho a 14 dias de vacaciones.");

            // De 7 a mas años de servicio 
            } else if (antiguedad >= 7) {
                System.out.println(nombre + " usted tiene derecho a 20 dias de vacaciones.");
            
            //Menos de un año de servicio
            } else {System.out.println(nombre + " usted no tiene derecho a vacaciones");}

        // Logistica
        } else if (clave == 2) {
            // 1 año de servicio
            if (antiguedad == 1) {
                System.out.println(nombre + " usted tiene derecho a 7 dias de vacaciones.");

            // De 2 a 6 años de servicio 
            } else if (antiguedad >= 2 && antiguedad <= 6) {
                System.out.println(nombre + " usted tiene derecho a 15 dias de vacaciones.");

            // De 7 a mas años de servicio 
            } else if (antiguedad >= 7) {
                System.out.println(nombre + " usted tiene derecho a 22 dias de vacaciones.");
            
            //Menos de un año de servicio
            } else {System.out.println(nombre + " usted no tiene derecho a vacaciones");}

        // Gerencia
        } else if (clave == 3) {
            // 1 año de servicio
            if (antiguedad == 1) {
                System.out.println(nombre + " usted tiene derecho a 10 dias de vacaciones.");

            // De 2 a 6 años de servicio 
            } else if (antiguedad >= 2 && antiguedad <= 6) {
                System.out.println(nombre + " usted tiene derecho a 20 dias de vacaciones.");

            // De 7 a mas años de servicio 
            } else if (antiguedad >= 7) {
                System.out.println(nombre + " usted tiene derecho a 30 dias de vacaciones.");
            
            //Menos de un año de servicio
            } else {System.out.println(nombre + " usted no tiene derecho a vacaciones");}
        
        // Solo son 3 claves
        } else {System.out.println("Error, la clave del departamento no existe");}

    }
}
