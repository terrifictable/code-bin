const bodyParser = require('body-parser');
const express = require('express');
const fs = require('fs');

const api = express();
api.use(bodyParser.json());

api.listen(5000, () => {
    console.log("API up and running (http://localhost:5000)");
});

let workingDir = "./data/"


api.post("/add", (req, res) => {
    console.log(req.body);
    let name = req.body['name'];
    let content = req.body['content'];
    let path = req.body['path'];
    let newpath = path.replace(' ', "_") + "/"

    if (newpath == "") { newpath = "/" }
    let tmppath = workingDir + newpath + name
    let finalpath = tmppath.replace("//", "/")
    
    fs.mkdir(workingDir, () => { "" })

    if (name != "" || name != None) {
        fs.mkdir(workingDir + path, () => { "succsess" })
        if (fs.existsSync(finalpath)) {
            res.send('File already exists')
        }
        fs.writeFileSync(finalpath, content)
        try {
            res.send("succsess");
        } catch { "" }
    }
    try { res.send('Invalid name') } catch { "" }
});
