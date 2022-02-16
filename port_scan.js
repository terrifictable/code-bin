const net = require("net");

if (process.argv.length == 6) {
    let min = parseInt(process.argv[3]);
    let max = parseInt(process.argv[4]);
    let ip = process.argv[2];
    let timeout = parseInt(process.argv[5]);

    function scan(n) {
        //  \033[92m    Green
        //  \033[93m    Orange

        if (n > max) process.exit(0);
        process.stdout.write('\033[93m' + ip + ' -> ' + n + '\033[97m');

        let s = net.createConnection(n, ip);
        s.setTimeout(timeout);

        s.on('connect', () => {
            process.stdout.write("\r\x1b[K");
            process.stdout.write("\033[92m" + ip + " -> " + n + "\033[97m\n");
            s.destroy();
            scan(n+1);
        });

        s.on('timeout', () => {
            process.stdout.write("\r\x1b[K");
            s.destroy();
            scan(n+1);
        });

        s.on('error', () => {
            process.stdout.write("\r\x1b[K");
            s.destroy();
            scan(n+1);
        });
    }
    scan(min);
}

// USAGE: node port_scan.js 127.0.0.1 1 65000 100
