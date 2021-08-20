const fs = require('fs');
const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const t = require("@babel/types");
const generator = require("@babel/generator").default;

const jscode = fs.readFileSync("./demo.js", {
        encoding: "utf-8"
    });
let ast = parser.parse(jscode);


// 打印四次，有两个函数节点
const visitor3 = {
    FunctionExpression: {
        enter(path) {
            console.log("xiaojianbang enter");
        },
        exit(path) {
            console.log("xiaojianbang exit");
        }
    }
};
traverse(ast, visitor3);

let code = generator(ast).code;
fs.writeFile('./demoNew.js', code, (err) => {});
