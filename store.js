function store_func(data, store) {
    let reset;
    if (store && !data) { reset = true; }
    else { reset = false; }

    let result = data && store;
    return result.toString() + ", " + reset.toString();
}


let var1 = store_func(true, true);
let var2 = store_func(true, false);
let var3 = store_func(false, false);
let var4 = store_func(false, true);

let out1 = "True, True";
let out2 = "True, False";
let out3 = "False, False";
let out4 = "False, True";
console.log("     Output      |  Function Input   |  Expected");
console.log("-----------------|-------------------|----------------");
console.log(var1+"      |  "+out1+"       |  True, True");
console.log(var2+"     |  "+out2+"      |  False, False");
console.log(var3+"     |  "+out3+"     |  False, False");
console.log(var4+"      |  "+out4+"      |  False, True");
