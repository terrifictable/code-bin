using System;
using System.IO;
using System.Threading;

namespace file_creator
{
    class Program
    {
        static void Main(string[] args)
        {
            string dirPath = Directory.GetCurrentDirectory();
            string[] folders = GetSubFolders(dirPath);


            foreach (string folder in folders) {
                if (Directory.Exists(folder)) {
                    CreateFiles(folder, "SUBFOLDERNAME", "FILENAME.EXTENTION", "FILECONTENT", 10);
                }
            }

        }

        public static string[] GetSubFolders(string path) {
            // Returns Sub Folders
            string[] folders = Directory.GetDirectories(path, "*", SearchOption.AllDirectories);
            return folders;
        }

        public static bool CreateFiles(string path, string foldername, string filename, string filecontent, int amount) {
            // Returns true on succsess otherwise false

            try {
                string pathString = System.IO.Path.Combine(path, foldername);
                System.IO.Directory.CreateDirectory(pathString);

                for (int i=0; i<amount; i++) {
                    string filepath = pathString + "/" + filename.Split(".")[0] + i + "." + filename.Split(".")[1];

                    File.WriteAllText(filepath, filecontent);
                }
            } catch { return false; }

            return true;
        }
    }
}
