/* NOTE: Graded 100/100
   NOTE: All tests pass */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

class Fifo {
  	queue = [];

    push(item) {
        this.queue[this.queue.length++] = item;
    }

  	pop() {
      	if (!this.queue.length) return undefined;

        const item = this.queue[0];
      	for (let i = 0; i < this.queue.length - 1; i++)
         	this.queue[i] = this.queue[i + 1];

      	this.queue.length--;
      	return item;
    }

}

const queue = new Fifo();
rl.on('line', line => {
    queue.push(line.split(" ")
    	.map(w => w[0].toUpperCase() + w.substring(1))
    	.join(" "));
});

rl.on('close', () => {
  	let line;
  	while (line = queue.pop())
    	console.log(line);
});