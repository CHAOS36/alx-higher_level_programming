#!usr/bin/node

const supSquare = require('./5-square');

class Square extends supSquare {
	charPrint (c) {
		if (c == null) {
			c = 'X';
		}
		for (let pipo = 0; pipo < this.width; pipo++) {
			console. log(c.repeat(this.width));
		}
	}
}

module.exports = Square;
