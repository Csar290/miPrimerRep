public class EjercicioPractico2 {
    public static void main(String[] args) {
        
        int incremento = 1, decremento = 100;

        while (incremento <= 5 && decremento >= 95) {

            System.out.print(incremento + ", ");
            incremento++;
            decremento--;

            if (decremento > 95) {
                System.out.print(decremento + ", ");
            } else {System.out.print(decremento);}
        }
    }
}
