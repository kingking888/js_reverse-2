function stringToByte(str) {
    var byteArr = [];
    for (var i = 0; i < str.length; i++) {
        byteArr.push(str.charCodeAt(i));
    }
    return byteArr;
}
x = stringToByte('xiaojianbang')
console.log(x);
console.log(x.toString());
// [120, 105, 97, 111, 106, 105, 97, 110, 98, 97, 110, 103]


// console.log(eval(String.fromCharCode(120, 105,  97, 111, 106,
//     105,  97, 110,  98,  97,
//     110, 103)));
//

x = stringToByte('console.log(x,"<<<<")')
console.log(x);
console.log(x.toString());




function aa(x){
    // console.log(x,"<<<<")
    eval(String.fromCharCode(99,111,110,115,111,108,101,46,108,111,103,40,120,44,34,60,60,60,60,34,41))
}

aa("哈哈哈哈")