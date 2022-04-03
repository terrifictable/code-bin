package burp;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;


public class BurpExtender implements IBurpExtender, IHttpListener, ITab {
    private IBurpExtenderCallbacks callbacks;
    private IExtensionHelpers helpers;
    private JTextField word_1_field;
    private JTextField word_2_field;
    private String word_1 = "";
    private String word_2 = "";
    private PrintWriter debug;
    private JPanel panel;


    @Override
    public void registerExtenderCallbacks(IBurpExtenderCallbacks callbacks) {
        this.callbacks = callbacks;
        this.helpers = callbacks.getHelpers();
        this.callbacks.setExtensionName("[ReplaceExt]");

        this.callbacks.registerHttpListener(this);


        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                panel = new JPanel();

                JLabel word_1_fieldlabel = new JLabel("Word to replace:  ");
                word_1_fieldlabel.setMaximumSize(new Dimension(200, word_1_fieldlabel.getPreferredSize().height));
                word_1_fieldlabel.setMinimumSize(new Dimension(200, word_1_fieldlabel.getPreferredSize().height));
                JLabel word_2_fieldlabel = new JLabel("Word to replace word with:  ");
                word_2_fieldlabel.setMaximumSize(new Dimension(200, word_1_fieldlabel.getPreferredSize().height));
                word_2_fieldlabel.setMinimumSize(new Dimension(200, word_1_fieldlabel.getPreferredSize().height));

                word_1_field = new JTextField();
                word_1_field.setText(word_1);
                word_1_field.setMaximumSize(new Dimension(300, word_1_field.getPreferredSize().height));
                word_1_field.setMinimumSize(new Dimension(300, word_1_field.getPreferredSize().height));
                word_1_field.setVisible(true);

                word_2_field = new JTextField();
                word_2_field.setText(word_1);
                word_2_field.setMaximumSize(new Dimension(300, word_2_field.getPreferredSize().height));
                word_2_field.setMinimumSize(new Dimension(300, word_2_field.getPreferredSize().height));
                word_2_field.setVisible(true);

                JButton updateButton = new JButton("Update");
                updateButton.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        word_1 = word_1_field.getText();
                        word_2 = word_2_field.getText();
                        debug.println("[ReplaceExt] [DEBUG] Word_1: " + word_1);
                        debug.println("[ReplaceExt] [DEBUG] Word_2: " + word_2);
                    }
                });

                GroupLayout layout = new GroupLayout(panel);
                panel.setLayout(layout);

                layout.setHorizontalGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup()
                                .addGroup(layout.createSequentialGroup()
                                        .addComponent(word_1_fieldlabel)
                                        .addComponent(word_1_field))
                                .addGroup(layout.createSequentialGroup()
                                        .addComponent(word_2_fieldlabel)
                                        .addComponent(word_2_field))
                                .addComponent(updateButton, GroupLayout.Alignment.TRAILING)));

                layout.setVerticalGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup()
                                .addComponent(word_1_fieldlabel)
                                .addComponent(word_1_field))
                        .addGroup(layout.createParallelGroup()
                                .addComponent(word_2_fieldlabel)
                                .addComponent(word_2_field))
                        .addComponent(updateButton));

                callbacks.customizeUiComponent(panel);
                callbacks.addSuiteTab(BurpExtender.this);
            }
        });


        this.debug = new PrintWriter(callbacks.getStdout(), true);
        this.debug.println("[ReplaceExt] Initialized");
    }
    

    @Override
    public void processHttpMessage(int toolFlag, boolean isRequest, IHttpRequestResponse messageInfo) {
        if (isRequest) {
            // Request
            IRequestInfo request = this.helpers.analyzeRequest(messageInfo.getHttpService(), messageInfo.getRequest());
            List<String> newHeaders = request.getHeaders();

            newHeaders.add("Replace-Word: " + word_1 + ":" + word_2);

            int bodyOffset = request.getBodyOffset();
            String body = new String(messageInfo.getRequest()).substring(bodyOffset);

            byte[] newRequest = this.helpers.buildHttpMessage(newHeaders, body.getBytes());
            this.debug.println("[ReplaceExt] [DEBUG] " + "Request");

            messageInfo.setRequest(newRequest);

        } else {
            // Response
            byte[] resp = messageInfo.getResponse();
            IResponseInfo responseData = helpers.analyzeResponse(resp);
            List<String> headers = responseData.getHeaders();
            String body = new String(Arrays.copyOfRange(resp, responseData.getBodyOffset(), resp.length));

            body = body.toLowerCase().replace(word_1, word_2);

            byte[] response = helpers.buildHttpMessage(headers, body.getBytes());
            this.debug.println("[ReplaceExt] [DEBUG] Response");

            messageInfo.setResponse(response);

        }
    }

    @Override
    public String getTabCaption() {
        return "ReplaceExt";
    }

    @Override
    public Component getUiComponent() {
        return this.panel;
    }
}
