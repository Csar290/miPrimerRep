import javax.swing.*;

public class InterfazGrafica1_1  extends JFrame {
    
    public InterfazGrafica1_1() {
        setLayout(null);
    }

    public static void main(String[] args) {
        InterfazGrafica1_1 formulario2 = new InterfazGrafica1_1();
        formulario2.setBounds(0,0,500,300);
        formulario2.setVisible(true);
        formulario2.setLocationRelativeTo(null);
        formulario2.setResizable(false);
    }
}
