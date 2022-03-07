using System;
using System.Text;


namespace hex
{
    class Program
    {
        public static bool url = false;

        static void Main(string[] args)
        {
            string? str;
            string? hex;
            


            Console.Clear();
            Console.WriteLine(" [1] Encode Hex\n [2] Decode Hex\n [3] Settings");
            Console.Write("Option: ");
            string? option = Console.ReadLine();

            try {
                if (option == "1") {
                    Console.Write("\n[?] String: ");
                    str = Console.ReadLine();

                    if (str != null) {
                        if (str != "" || str != " ") {
                            if (url == true) {
                                Console.WriteLine("[+] Hex: https://%" + StrToHex(str).Replace(" ", "%"));
                                Console.ReadKey();
                            } else {
                                Console.WriteLine("[+] Hex: " + StrToHex(str));
                                Console.ReadKey();
                            }
                        } else {
                            Console.WriteLine("[-] Invalid Input: '" + str + "'");
                            Console.ReadKey();
                        }
                    }

                } else if (option == "2") {
                    Console.Write("\nHex: ");
                    hex = Console.ReadLine();

                    if (hex != null) {
                        if (hex != "" || hex != " ") {
                            Console.WriteLine("[?] String: " + HexToStr(hex));
                            Console.ReadKey();
                        } else {
                            Console.WriteLine("[-] Invalid Input: '" + hex + "'");
                            Console.ReadKey();
                        }
                    } 

                } else if (option == "3") {
                    Console.WriteLine("\n\n---SETTINGS---");
                    Console.WriteLine(" URL Encoding: " + url.ToString());
                    Console.WriteLine("--------------\n");

                    Console.Write("[+] Toggle 'URL Encoding' [y/n]");
                    string? toggle = Console.ReadLine();

                    if (toggle != null) {
                        if (toggle.ToLower() == "y") {
                            url = true;

                            Console.WriteLine("\n[+] Press any key to continue");
                            Console.ReadKey();
                            Main(args);
                        } else {
                            Console.WriteLine("\n[+] Press any key to continue");
                            Console.ReadKey();
                            Main(args);
                        }

                    } else {
                        Console.WriteLine("[-] Invalid Input\n  Press [ENTER] to return");
                        Console.ReadKey();
                        Main(args);
                    }
                }
            } catch (Exception e) {
                Console.WriteLine("[-] Error: " + e);
            }
        }

        static string StrToHex(string str)
        {
            if (str == null) { return "\"" + str + "\" cant be null"; }

            byte[] bytearray = Encoding.Default.GetBytes(str);
            var hexString = BitConverter.ToString(bytearray);

            return hexString.Replace("-", " ").ToString();
        }

        static string HexToStr(string hex)
        {
            if (hex == null) { return "\"" + hex + "\" cant be null"; }

            hex = hex.Replace(" ", "").Replace("-", "");
            byte[] raw = new byte[hex.Length / 2];
            for (int i = 0; i < raw.Length; i++) {
                raw[i] = Convert.ToByte(hex.Substring(i * 2, 2), 16);
            }

            return Encoding.ASCII.GetString(raw).ToString();
        }
    }
}
