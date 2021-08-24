const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generator = require("@babel/generator").default;
const fs = require('fs');

const jscode = fs.readFileSync("./demo.js", {
        encoding: "utf-8"
    });
let ast = parser.parse(jscode);
function base64Encode(e) {
	var r, a, c, h, o, t, base64EncodeChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
	for (c = e.length, a = 0, r = ''; a < c;) {
		if (h = 255 & e.charCodeAt(a++), a == c) {
			r += base64EncodeChars.charAt(h >> 2),
				r += base64EncodeChars.charAt((3 & h) << 4),
				r += '==';
			break
		}
		if (o = e.charCodeAt(a++), a == c) {
			r += base64EncodeChars.charAt(h >> 2),
				r += base64EncodeChars.charAt((3 & h) << 4 | (240 & o) >> 4),
				r += base64EncodeChars.charAt((15 & o) << 2),
				r += '=';
			break
		}
		t = e.charCodeAt(a++),
			r += base64EncodeChars.charAt(h >> 2),
			r += base64EncodeChars.charAt((3 & h) << 4 | (240 & o) >> 4),
			r += base64EncodeChars.charAt((15 & o) << 2 | (192 & t) >> 6),
			r += base64EncodeChars.charAt(63 & t)
	}
	return r
}

traverse(ast, {
	FunctionExpression(path){
		let blockStatement = path.node.body;
		let Statements = blockStatement.body.map(function(v){
			if(t.isReturnStatement(v)) return v;
			let code = generator(v).code;
			let cipherText = base64Encode(code);
			let decryptFunc = t.callExpression(t.identifier('atob'), [t.stringLiteral(cipherText)]);
			return t.expressionStatement(t.callExpression(t.identifier('eval'), [decryptFunc]));
		});
		path.get('body').replaceWith(t.blockStatement(Statements));
	}
});

let code = generator(ast).code;
fs.writeFile('./demoNew.js', code, (err)=>{});
