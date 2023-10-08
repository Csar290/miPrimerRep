public class EjercicioPractico3 {
    public static void main(String[] args) {
        
        int a = 0, b = 1, suma = 0;
        for (int i = 0; i < 10; i++) {

            if (suma < 35) {
                System.out.print(a + ", ");
                suma = a + b;
                a = b;
                b = suma;
            } else {System.out.print(a);}

        }
    }
}