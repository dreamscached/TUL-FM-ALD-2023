/* NOTE: Graded 100/100
   NOTE: All tests pass */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

class Lifo {
  	#stack = [];

    push(item) {
        this.#stack[this.#stack.length++] = item;
    }

  	pop() {
      	const item = this.#stack[this.#stack.length - 1];
      	if (this.#stack.length) this.#stack.length--;
      	return item;
    }
}

const stack = new Lifo();
rl.on('line', line => {
    stack.push(line.split(" ")
    	.map(w => w[0].toUpperCase() + w.substring(1))
    	.join(" "));
});

rl.on('close', () => {
  	let line;
  	while (line = stack.pop())
    	console.log(line);
});

