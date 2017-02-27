/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Froms;

import static Froms.Lista.webClient;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.net.MalformedURLException;
import java.net.URL;
import javax.swing.JOptionPane;

/**
 *
 * @author jhonny
 */
public class Cola extends javax.swing.JFrame {
    private Principal p;
    /**
     * Creates new form Cola
     * @param p
     */
    public Cola(Principal p) {
        this.p = p;
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Cola.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Cola.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Cola.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Cola.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        txtunico = new javax.swing.JTextField();
        jbque = new javax.swing.JButton();
        jbdeq = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent evt) {
                cerrado(evt);
            }
        });

        txtunico.setFont(new java.awt.Font("Comic Sans MS", 0, 14)); // NOI18N
        txtunico.setHorizontalAlignment(javax.swing.JTextField.CENTER);

        jbque.setFont(new java.awt.Font("Comic Sans MS", 0, 13)); // NOI18N
        jbque.setText("queue");
        jbque.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jbqueActionPerformed(evt);
            }
        });

        jbdeq.setFont(new java.awt.Font("Comic Sans MS", 0, 13)); // NOI18N
        jbdeq.setText("dequeue");
        jbdeq.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jbdeqActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(68, 68, 68)
                        .addComponent(txtunico, javax.swing.GroupLayout.PREFERRED_SIZE, 200, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(123, 123, 123)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jbdeq, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jbque, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE))))
                .addContainerGap(72, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(33, 33, 33)
                .addComponent(txtunico, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(20, 20, 20)
                .addComponent(jbque, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(20, 20, 20)
                .addComponent(jbdeq, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(25, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void cerrado(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_cerrado
        // TODO add your handling code here:
        this.setVisible(false);
        p.setVisible(true);
    }//GEN-LAST:event_cerrado

    private void jbqueActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jbqueActionPerformed
        // TODO add your handling code here:
        if(!txtunico.getText().equals("")){
            RequestBody rb = new FormEncodingBuilder()
                .add("dato", txtunico.getText())
                .build();
            String print = getString("queueCola", rb);
            //System.out.println(print);
            JOptionPane.showMessageDialog(null, "valor numerico: "+ txtunico.getText());//+ " indice " + print + " agregado");
            txtunico.setText("");
        }
    }//GEN-LAST:event_jbqueActionPerformed

    private void jbdeqActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jbdeqActionPerformed
        // TODO add your handling code here:
        RequestBody rb = new FormEncodingBuilder()
                .add("dato", "unico")
                .build();
            String print = getString("deQueueCola", rb);
            System.out.println("DATO DESENCOLADO "+ print);
            //JOptionPane.showMessageDialog(null, "valor numerico "+ txtunico.getText() + " indice " + print + " agregado");
            txtunico.setText("");
    }//GEN-LAST:event_jbdeqActionPerformed

    public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            //java.util.logging.Logger.getLogger(.log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            //java.util.logging.Logger.getLogger(testwebserver.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jbdeq;
    private javax.swing.JButton jbque;
    private javax.swing.JTextField txtunico;
    // End of variables declaration//GEN-END:variables
}
