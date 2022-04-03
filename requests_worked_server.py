const express = require("express");
app = express();

var requests = 0;

app.listen(5000, () => {
  console.log("APP running (http://localhost:5000)");
});

try {
  app.get("/", (req, res) => {
    if (requests >= 10) {
      res.send('{"views": ' + requests + ', "succsess": 0}');
      console.log("RESET");
      requests = 0;
    }
    requests++;
    console.log(requests);
    res.send('{"views": ' + requests + ', "succsess": 1}');  // sometimes just gives you an error, the "try { ... } catch { ... }" doesnt work i dont know how to fix it
  });
} catch {
  console.log("ERROR");
}
