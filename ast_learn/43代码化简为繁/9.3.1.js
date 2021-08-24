const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generator = require("@babel/generator").default;
const fs = require('fs');

const jscode = fs.readFileSync("./demo.js", {
        encoding: "utf-8"
    });
let ast = parser.parse(jscode);

traverse(ast, {
	BinaryExpression(path){
		let operator = path.node.operator;
		let left = path.node.left;
		let right = path.node.right;
		let a = t.identifier('a');
		let b = t.identifier('b');
		// // 创建一个上下文中新的引用 生成类似于{ type: 'Identifier', name: '_n2' }
		let funcNameIdentifier = path.scope.generateUidIdentifier('xxx');
		let func = t.functionDeclaration(
			funcNameIdentifier, 
			[a, b], 
			t.blockStatement([t.returnStatement(
					t.binaryExpression(operator, a, b)
				)]));
		let BlockStatement = path.findParent(
					function(p){return p.isBlockStatement()});
		BlockStatement.node.body.unshift(func);
		path.replaceWith(t.callExpression(funcNameIdentifier, [left, right]));
	}
});

let code = generator(ast).code;
fs.writeFile('./demoNew.js', code, (err)=>{});
