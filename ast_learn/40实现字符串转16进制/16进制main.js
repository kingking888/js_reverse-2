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

let bigArr = [];
traverse(ast, {
    StringLiteral(path){
        let cipherText = base64Encode(path.node.value);
        let bigArrIndex = bigArr.indexOf(cipherText);
        let index = bigArrIndex;
        if(bigArrIndex == -1){
            let length = bigArr.push(cipherText);
            index = length -1;
        }
        let encStr = t.callExpression(
            t.identifier('atob'),
            [t.memberExpression(t.identifier('arr'),
                t.numericLiteral(index), true)]);
        path.replaceWith(encStr);
    }
});

(function (myArr, num){
    var xiaojianbang = function (nums){
        while (--nums){
            myArr.unshift(myArr.pop())
        }
    };
    xiaojianbang(++num);
})(bigArr, 0x10);





bigArr = bigArr.map(function(v){
    return t.stringLiteral(v);
});
//????????????????????????
bigArr = t.variableDeclarator(t.identifier('arr'), t.arrayExpression(bigArr));
bigArr = t.variableDeclaration('var', [bigArr]);

//????????????????????????????????????????????????astFront
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

traverse(astFront,{
    MemberExpression(path){
        if(t.isIdentifier(path.node.property)){
            let name = path.node.property.name;
            path.node.property = t.stringLiteral(hexEnc(name));
        }
        path.node.computed = true;
    }
});

//???????????????????????????????????????????????????????????????ast???
ast.program.body.unshift(astFront.program.body[0]);
//?????????????????????????????????ast?????????
ast.program.body.unshift(bigArr);
let code = generator(ast).code;

code = code.replace(/\\\\x/g,"\\x")     // ???????????????
fs.writeFile('./demoNew.js', code, (err)=>{});
