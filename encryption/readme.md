Base64, Base85/Ascii85, Rot: Encryption and decryption<br>

[Main.java]()

<pre><code>
Normal:
  - Base85/ASCII85    encryption and decryption (concept (in c#) from google)
  - Base64            encryption and decryption
  - Rot               encryption and decryption

Combined:
  - Base85 & Base64   encryption and decryption
  - Base64 & Rot      encryption and decryption
  
Examples:
  Normal:
    - Rot:
      class      function   string         rot offset
      RotEncoder.RotEncode("Hello World", 18);
      RotDecoder.RotDecode("Zw447 o704v", 18);

    - Base64:
      class         function      string
      Base64Encoder.Base64Encode("Hello World!");
      Base64Decoder.Base64Decode("SGVsbG8gV29ybGQh");

    - Base85:
      class         function      string
      Base85Encoder.Base85Encode("Hello World!");
      Base85Decoder.Base85Decode("87cURD]i,\"Ebo80");
  
  Combined:
    - Base64 & Rot
      class         function         string             rot offset
      Base64Encoder.Base64RotEncode("Hello World!",     18);
      Base64Decoder.Base64RotDecode("Wnc0NDcgbzcwNHZJ", 18);

    - Base85 & Base64:
      class         function          string
      Base85Encoder.Base85_64Encoder("Hello World!");
      Base85Decoder.Base85_64Decode( "ODdjVVJEXWksIkVibzgw");
  
</code></pre>
