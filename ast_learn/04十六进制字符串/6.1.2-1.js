function hexEnc(code) {
    for (var hexStr = [], i = 0, s; i < code.length; i++) {
        // s = code.charCodeAt(i)
        // console.log("默认Unicode编码>", s)
        // s = code.charCodeAt(i).toString(10);
        // console.log("转成10进制Unicode编码>", s)
        s = code.charCodeAt(i).toString(16);
        // console.log("转成16进制Unicode编码>", s)
        hexStr += "\\x" + s;
    }
    return hexStr
}
// 汉字转十六进制

text1 = hexEnc("中文")

text1 = hexEnc("yyyy-MM-dd")
console.log(text1)



function decode(str){
    return str.replace(/\\x(\w{2})/g,function(_,$1){ return String.fromCharCode(parseInt($1,16)) });
}

console.log(decode(text1))

console.log("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")