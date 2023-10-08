public class Condicionales {
    public static void main(String[] args){

        int matematica = 10, biologia = 16, quimica = 14, promedio = (matematica + biologia + quimica) / 3;
        
        //Condición
        if (promedio >= 12) {
            System.out.println("Aprobaste");
            //Anidación de condicionales
            if (promedio == 12) {
                System.out.println("Pero raspando con: " + promedio);
            } else if (promedio == 13) {
                System.out.println("con: " + promedio + " Se puede mejorar.");
            } else if (promedio == 14) {
                System.out.println("con: " + promedio + " Nada mal.");
            } else if (promedio == 15) {
                System.out.println("con: " + promedio + " Bien hecho.");
            } else if (promedio >= 16) {
                System.out.println("con: " + promedio + " Excelente, sigue asi.");
            }
        } else {System.out.println("Desaprobaste con: " + promedio + " Esfuerzate mas.");}
    }
}

