const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generator = require("@babel/generator").default;
const fs = require('fs');

const jscode = fs.readFileSync("./demo.js", {
        encoding: "utf-8"
    });
let ast = parser.parse(jscode);


//读取还原数组顺序的函数，并解析成astFront
const jscodeFront = fs.readFileSync("./demoFront.js", {
    encoding: "utf-8"
});
let astFront = parser.parse(jscodeFront);


function hexEnc(code) {
    for (var hexStr = [], i = 0, s; i < code.length; i++) {
        s = code.charCodeAt(i).toString(16);
        hexStr += "\\x" + s;
    }
    return hexStr
}


// traverse(astFront,{
// 	MemberExpression(path){
// 		if(t.isIdentifier(path.node.property)){
// 			let name = path.node.property.name;
// 			path.node.property = t.stringLiteral(hexEnc(name));
// 		}
// 		path.node.computed = true;
// 	}
// });
traverse(ast,{
    MemberExpression(path){
        if(t.isIdentifier(path.node.property)){
            let name = path.node.property.name;
            path.node.property = t.stringLiteral(hexEnc(name));
        }
        path.node.computed = true;
    }
});


// let code1 = generator(astFront).code;
// console.log(code1);

let code = generator(ast).code;
fs.writeFile('./demoNew.js', code, (err)=>{});
