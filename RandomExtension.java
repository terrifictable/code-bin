package burp;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

public class BurpExtender implements IBurpExtender, IHttpListener, ITab
{
    private IBurpExtenderCallbacks callbacks;
    private IExtensionHelpers helpers;
    private PrintWriter debug;
    private JPanel panel;
    private JTextField passwordField;
    private String password = "DEFAULT";

    @Override
    public void registerExtenderCallbacks(IBurpExtenderCallbacks callbacks) {
        this.callbacks = callbacks;
        this.helpers = callbacks.getHelpers();
        this.callbacks.setExtensionName("RandomExtension");

        this.callbacks.registerHttpListener(this);

        SwingUtilities.invokeLater(new Runnable() {

            @Override
            public void run() {
                panel = new JPanel();

                JLabel passwordFieldLabel = new JLabel("Password:  ");

                passwordField = new JTextField();
                passwordField.setText(password);
                passwordField.setMaximumSize(new Dimension(300, passwordField.getPreferredSize().height));
                passwordField.setMinimumSize(new Dimension(300, passwordField.getPreferredSize().height));
                passwordField.setVisible(true);

                JButton passwordButton = new JButton("Update");
                passwordButton.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        password = passwordField.getText();
                        debug.println(password);
                    }
                });

                GroupLayout layout = new GroupLayout(panel);
                panel.setLayout(layout);

                layout.setHorizontalGroup(layout.createSequentialGroup()
                            .addGroup(layout.createParallelGroup()
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(passwordFieldLabel)
                                        .addComponent(passwordField)
                                    )
                                    .addComponent(passwordButton, GroupLayout.Alignment.TRAILING)
                            )
                );

                layout.setVerticalGroup(layout.createSequentialGroup()
                            .addGroup(layout.createParallelGroup()
                                    .addComponent(passwordFieldLabel)
                                    .addComponent(passwordField)
                            )
                            .addComponent(passwordButton)
                );


                callbacks.customizeUiComponent(panel);
                callbacks.addSuiteTab(BurpExtender.this);
            }
        });

        this.debug = new PrintWriter(callbacks.getStdout(), true);
        this.debug.println("[RandomExtension] Initialized");
    }


    @Override
    public void processHttpMessage(int toolFlag, boolean isRequest, IHttpRequestResponse messageInfo) {
        if (isRequest) {
            // this.debug.println("> Intercepted Request");
            if (this.callbacks.TOOL_REPEATER == toolFlag) {
                IRequestInfo request = this.helpers.analyzeRequest(messageInfo.getHttpService(), messageInfo.getRequest());
                List<String> newHeaders = request.getHeaders();

                String path = messageInfo.getUrl().getPath();
                String query = messageInfo.getUrl().getQuery();
                String uri = "";

                if (query == null) {
                    query = "";
                    uri = path + password;
                } else {
                    uri = path + "?" + query + password;
                }

                MessageDigest digest = null;
                try {
                    digest = MessageDigest.getInstance("SHA-256");
                } catch (NoSuchAlgorithmException e) {
                    e.printStackTrace();
                }
                byte[] encodedhash = digest.digest(uri.getBytes(StandardCharsets.UTF_8));
                String authToken = this.helpers.base64Encode(encodedhash);

                debug.println(authToken);

                newHeaders.add("X-Custom-Header: " + authToken);

                int bodyOffset = request.getBodyOffset();
                String body = new String(messageInfo.getRequest()).substring(bodyOffset);

                byte[] newRequest = this.helpers.buildHttpMessage(newHeaders, body.getBytes());
                messageInfo.setRequest(newRequest);
            }
        }
    }

    @Override
    public String getTabCaption() {
        return "RandomExtension";
    }

    @Override
    public Component getUiComponent() {
        return this.panel;
    }
}
