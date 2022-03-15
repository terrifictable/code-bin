const bodyParser = require("body-parser");
const express = require("express");
const fs = require("fs");

const api = express();
api.use(bodyParser.json());
let workingDir = "./data/";

api.listen(5000, () => {
  console.log("API up and running (http://localhost:5000)");
});

api.get("/:folder", (req, res) => {
  try {
    fs.readdir("./" + req.params.folder.replace(":", "").replace("_", "/") + "/", (err, files) => {
      //   const new_files = [];
      let new_files = "";
      files.forEach((file, _, __) => {
        // new_files.push(file + "<br>");
        new_files += "<a href='/file/:" + req.params.folder.replace(":", "") + "_" + file + "'>" + file + "</a><br>";
      });
      res.send("<h1>Files</h1><hr><br><h3>" + new_files);
    });
  } catch (e) {
    ("");
  }
});

api.get("/file/:file", (req, res) => {
  let file = req.params.file.replace(":", "").replace("_", "/");
  fs.readFile("./" + file, "utf-8", (err, content) => {
    res.send("<h1>File ./" + file + "</h1><hr><br>" + content + "<br><br><br><br><br><br><a href='/:'>Back</a>");
  });
});

api.post("/add", (req, res) => {
  console.log(req.body);
  let name = req.body["name"];
  let content = req.body["content"];
  let path = req.body["path"];
  let newpath = path.replace(" ", "_") + "/";

  if (newpath == "") {
    newpath = "/";
  }
  let tmppath = workingDir + newpath + name;
  let finalpath = tmppath.replace("//", "/");

  fs.mkdir(workingDir, () => {
    "";
  });

  if (name != "" || name != None) {
    fs.mkdir(workingDir + path, () => {
      "succsess";
    });
    if (fs.existsSync(finalpath)) {
      res.send("File already exists");
    }
    fs.writeFileSync(finalpath, content);
    try {
      res.send("succsess");
    } catch {
      ("");
    }
  }
  try {
    res.send("Invalid name");
  } catch {
    ("");
  }
});
