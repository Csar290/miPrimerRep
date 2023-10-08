import javax.swing.*;
import java.awt.event.*;

public class InterfazGrafica2_1 extends JFrame implements ActionListener {
    private JTextField textfield1;
    private JLabel etiqueta1;
    private JButton boton1, boton2;

    public InterfazGrafica2_1() {
        setLayout(null);
        etiqueta1 = new JLabel("Usuario:");
        etiqueta1.setBounds(10,10,100,30);
        add(etiqueta1);

        textfield1 = new JTextField();
        textfield1.setBounds(80,17,150,20);
        add(textfield1);

        boton1 = new JButton("Aceptar");
        boton1.setBounds(55,80,90,30);
        add(boton1);
        boton1.addActionListener(this);

        boton2 = new JButton("Cerrar");
        boton2.setBounds(180,80,90,30);
        add(boton2);
        boton2.addActionListener(this);
    }

    public void actionPerformed(ActionEvent click) {
        if (click.getSource() == boton1) {
            String text = textfield1.getText();
            setTitle(text);
        } if (click.getSource() == boton2) {
            System.exit(0);
        }
    }
    public static void main(String[] args) {
        InterfazGrafica2_1 formulario6 = new InterfazGrafica2_1();
        formulario6.setBounds(0,0,350,200);
        formulario6.setVisible(true);
        formulario6.setResizable(false);
        formulario6.setLocationRelativeTo(null);
    }
}
