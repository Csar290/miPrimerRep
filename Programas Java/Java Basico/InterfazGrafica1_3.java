import javax.swing.*;
import java.awt.event.*;

public class InterfazGrafica1_3 extends JFrame implements ActionListener {
    
    public static void main(String[] args) {
        InterfazGrafica1_3 formulario4 = new InterfazGrafica1_3();
        formulario4.setBounds(0, 0, 400, 400);
        formulario4.setVisible(true);
        formulario4.setResizable(false);
        formulario4.setLocationRelativeTo(null);
    }
    JButton boton1;
    public InterfazGrafica1_3() {
        setLayout(null);
        boton1 = new JButton("Cerrar");
        boton1.setBounds(250, 250, 100, 30);
        add(boton1);
        boton1.addActionListener(this);
    }
    public void actionPerformed(ActionEvent click) {
        if (click.getSource() == boton1)  {
            System.exit(0);
        }
    }
}
