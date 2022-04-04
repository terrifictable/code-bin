package me.terrifictable.examples;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.util.List;

public class Main {
    private static String title = "TerrificTable"; // title variable
    private static boolean resizable = false; // resizable variable
    // Both title"" and "resizable" don't need ot be variables, I just put them here as variables

    public static void main(String[] args) {

        Border border = BorderFactory.createLineBorder(new Color(102, 0, 255), 1); // Border
        Color backgroundColor = new Color(221, 226, 250, 255); // background color (doesn't need to be a variable)
        Dimension size = new Dimension(420, 420); // size for window (doesn't need to be a variable)

        // ================= FRAME =====================
        JFrame frame = new JFrame(); // creating window/frame
        frame.setTitle(title); // setting window title

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // close option (normally its "HIDE_ON_CLOSE" which will not exit the program)
        frame.setResizable(resizable); // if window is resizable or not

        frame.setSize((int) size.getWidth(), (int) size.getHeight()); // setting window size
        frame.setVisible(true); // if false or removed window will not be shown/created

        frame.getContentPane().setBackground(backgroundColor); // Setting background color of frame/window


        // ================= LABEL =======================
        // Adding Text to `frame`
        JLabel label = new JLabel(); // creating a new (J)Label
        label.setText("Example texT"); // change to whatever text you want to be displayed
        label.setHorizontalAlignment(JLabel.CENTER); // Horizontal Alignment
        label.setVerticalAlignment(JLabel.TOP); // Vertical Alignment
        label.setForeground(new Color(1, 1, 28)); // Text color
        label.setFont(new Font("Okami", Font.BOLD, 50)); // change front incase you don't have "Okami" font installed on your device
        label.setBorder(border); // adding border to Label (entire window in this case)

        frame.add(label); // adding `label` to frame
    }
}
