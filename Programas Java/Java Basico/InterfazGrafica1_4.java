import javax.swing.*;
import java.awt.event.*;

public class InterfazGrafica1_4 extends JFrame implements ActionListener {
    private JButton boton1, boton2, boton3, boton4;
    private JLabel label1;

    public InterfazGrafica1_4() {
        setLayout(null);
        boton1 = new JButton("1");
        boton1.setBounds(15,100,90,30);
        add(boton1);
        boton1.addActionListener(this);

        boton2 = new JButton("2");
        boton2.setBounds(150,100,90,30);
        add(boton2);
        boton2.addActionListener(this);

        boton3 = new JButton("3");
        boton3.setBounds(280,100,90,30);
        add(boton3);
        boton3.addActionListener(this);

        boton4 = new JButton("Cerrar");
        boton4.setBounds(280,20,90,30);
        add(boton4);
        boton4.addActionListener(this);

        label1 = new JLabel("En espera...");
        label1.setBounds(10,20,300,30);
        add(label1);
    }

    public void actionPerformed(ActionEvent click) {
        if (click.getSource() == boton1) {
            label1.setText("Has presionado el boton 1");
        } else if (click.getSource() == boton2) {
            label1.setText("Has presionado el boton 2");
        } else if (click.getSource() == boton3) {
            label1.setText("Has presionado el boton 3");
        } else if (click.getSource() == boton4)  {
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        InterfazGrafica1_4 formulario5 = new InterfazGrafica1_4();
        formulario5.setBounds(0,0,400,200);
        formulario5.setVisible(true);
        formulario5.setResizable(false);
        formulario5.setLocationRelativeTo(null);
    }
}
