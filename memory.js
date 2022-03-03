const os = require('os');

function roundUp(num, precision) {
    precision = Math.pow(10, precision);
    return Math.ceil(num * precision) / precision;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const Memory = async () => {
    await sleep(1000);
    let freemem = (os.freemem() / 1024 / 1024 / 1024);
    let totalmem = (os.totalmem() / 1024 / 1024 /1024);
    let leftmem = (totalmem - freemem);
  
    console.log("Total Memory: " + roundUp(totalmem, 1) + "GB");
    console.log("Free Memory: " + roundUp(freemem, 1) + "GB");
    console.log("Used Memory: " + roundUp(leftmem, 1) + "GB");
}
Memory()
