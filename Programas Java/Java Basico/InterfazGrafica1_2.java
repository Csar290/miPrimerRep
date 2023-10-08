import javax.swing.*;

public class InterfazGrafica1_2 extends JFrame {

    private JLabel etiqueta1;
    private JLabel etiqueta2;

    public InterfazGrafica1_2() {
        setLayout(null);
        etiqueta1 = new JLabel("Etiqueta numero uno");
        etiqueta1.setBounds(10,0,200,300);
        add(etiqueta1);
        etiqueta2 = new JLabel("Etiqueta numero dos");
        etiqueta2.setBounds(200,0,200,300);
        add(etiqueta2);
    }

    public static void main(String[] args) {
        InterfazGrafica1_2 formulario3 = new InterfazGrafica1_2();
        formulario3.setBounds(0,0,500,300);
        formulario3.setVisible(true);
        formulario3.setLocationRelativeTo(null);
        formulario3.setResizable(false);
    }
}
