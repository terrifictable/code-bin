const fs = require('fs');
const path = require('path');
let currentPath = "./" + process.argv[2];
console.log(currentPath);

fs.readdir(currentPath, (err, files) => {
    files.forEach(processFile);
});

function processFile(file) {
    let extention = path.extname(file);

    fs.mkdir(currentPath + extention, () => {
        fs.rename(currentPath + file, currentPath + extention + "/" + file, () => {
            console.log(currentPath + extention + "/" + file);
        });
    });
}
