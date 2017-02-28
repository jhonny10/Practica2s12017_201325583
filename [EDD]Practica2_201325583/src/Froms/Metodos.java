/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Froms;

import java.awt.Image;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import javax.swing.ImageIcon;

/**
 *
 * @author jhonny
 */
public class Metodos {
    public static Image icono(String url, int width, int heigth){
        ImageIcon ico = new ImageIcon(url);
        Image img = ico.getImage();
        Image imagen = img.getScaledInstance(width, heigth, Image.SCALE_SMOOTH);
        return imagen;
    }
    
    public static void eliminar_image_txt(String pathtxt, String pathImg){
        File f = new File(pathtxt);
        f.delete();
        File fimg = new File(pathImg);
        fimg.delete();
    }
    
    public static String generarTxt(String path, String in){
        File f = new File("C:\\txtDot\\" + path + ".txt");//"C:\\Users\\usuario\\Desktop\\ejemplo.txt");//, nodos + "}");
        try{
                FileWriter fw = new FileWriter(f, false);
                BufferedWriter br = new BufferedWriter(fw);
                br.write(in);
                br.close();
                fw.close();
        }catch(Exception e){
            
        }
        return f.getPath();
    }
    
    public static String generarImagen(String pathTxt, String nombreImg){
        String pathImagen = "";
        try{
            String dopath = "C:\\release\\bin\\dot.exe";
            String architxt = pathTxt; //"C:\\txtDot\\" + path + ".txt";//path;//"C:\\Users\\usuario\\Desktop\\ejemplo.txt";
            pathImagen = "C:\\imgDot\\" + nombreImg + ".png";
            String parpng = "-Tpng";
            String paro = "-o";
               
            String cmd[] = new String[5];
            cmd[0] = dopath;
            cmd[1] = parpng;
            cmd[2] = architxt;
            cmd[3] = paro;
            cmd[4] = pathImagen;
              
            Runtime rt = Runtime.getRuntime();
            rt.exec(cmd);
        }catch(Exception e){
            System.out.println(e.toString());
        }
        return pathImagen;
    }
}
