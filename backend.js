const { spawn } = require('child_process');
const python = spawn('python', ['backend.py']);

python.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
    let pub_key = String(data).split(" ");
    console.log(pub_key);
});

python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
});

python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});