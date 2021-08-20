const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generator = require("@babel/generator").default;
const fs = require('fs');

const jscode = fs.readFileSync("./demo.js", {
        encoding: "utf-8"
    });
let ast = parser.parse(jscode);


// path.parent  = path.parentPath.node

traverse(ast, {
	Identifier(path){
		let name = path.node.name;
		// console.log("name_node", name)
		// console.log()
		// console.log("path>>>1", path.node)
		// if (path.node.getParameters()){
		// 	console.log("path>>>2", path.node.paramName)
		//
		// }
		if (path.parent.params){
			return
		}
		if('eval|parseInt|encodeURIComponent|Object|Function|Boolean|Number|Math|Date|String|RegExp|Array'.indexOf(name) != -1){
			path.replaceWith(t.memberExpression(t.identifier('window'), t.stringLiteral(name), true));
		}
	}
});

let code = generator(ast).code;
console.log(code)
// fs.writeFile('./demoNew.js', code, (err)=>{});
