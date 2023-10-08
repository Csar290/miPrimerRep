import javax.swing.*;

public class InterfazGrafica extends JFrame{
    private JLabel etiqueta1;

    public InterfazGrafica() {
        setLayout(null);
        etiqueta1 = new JLabel("Mojang");
        etiqueta1.setBounds(210,0,200,300);
        add(etiqueta1);
    }

    public static void main(String[] args) {
        InterfazGrafica formulario1 = new InterfazGrafica();
        formulario1.setBounds(0,0,500,300);
        formulario1.setVisible(true);
        formulario1.setLocationRelativeTo(null);
    }
}
