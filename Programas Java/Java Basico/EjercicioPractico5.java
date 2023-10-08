import java.util.Scanner;

public class EjercicioPractico5 {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        String usuario = "Anizhetho", password = "";

        System.out.println("******************");
        System.out.println("*Inicio de sesion*");
        System.out.println("******************\n");
        
        System.out.print("Ingrese su nombre de usuario: ");
        usuario = input.nextLine();

        System.out.print("\nIngrese su contraseña: ");
        password = input.nextLine();

        if(usuario.equals("Anizhetho") && password.equals("123456")) {
            System.out.println("\nInició sesión correctamente");
        } else {System.out.println("\nSu nombre de usuario o contraseña son incorrectas");}

    }
}