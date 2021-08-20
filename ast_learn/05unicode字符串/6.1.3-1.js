function unicodeEnc(str) {
    var value = '';
    for (var i = 0; i < str.length; i++)
        value += "\\u" + ("0000" + parseInt(str.charCodeAt(i)).toString(16)).substr(-4);
    return value;
}
console.log(unicodeEnc("中国"));

// 与之前十六进制区别
//
// function hexEnc(code) {
//     for (var hexStr = [], i = 0, s; i < code.length; i++) {
//         // s = code.charCodeAt(i)
//         // console.log("默认Unicode编码>", s)
//         // s = code.charCodeAt(i).toString(10);
//         // console.log("转成10进制Unicode编码>", s)
//         s = code.charCodeAt(i).toString(16);
//         // console.log("转成16进制Unicode编码>", s)
//         hexStr += "\\x" + s;
//     }
//     return hexStr
// }
//
//
// console.log(hexEnc("中国"));