const os = require('os');
const fs = require('fs');

function roundUp(num, precision) {
    precision = Math.pow(10, precision);
    return Math.ceil(num * precision) / precision;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const freeMemory = async () => {
    for ( i = 0; i<10; i++) {
        await sleep(1000);
        let mem = ((os.freemem().toString() / 1024) / 1024) / 1024;
        let memory = roundUp(mem, 1);
        console.clear()
        console.log("Free Memory: " + memory + "GB");
    }
}
freeMemory()
