window = {}
Date.prototype.format = function (formatStr) {
    var str = formatStr;
    var Week = ['日', '一', '二', '三', '四', '五', '六'];
    str = str['replace'](/yyyy|YYYY/, this['getFullYear']());
    str = str['replace'](/MM/, (this['getMonth']() + 1) > 9 ? (this['getMonth']() + 1)['toString']() : '0' + (this['getMonth']() + 1));
    str = str['replace'](/dd|DD/, this['getDate']() > 9 ? this['getDate']()['toString']() : '0' + this['getDate']());
    return str
}
console.log(new window['Date']()['format']('\x79\x79\x79\x79\x2d\x4d\x4d\x2d\x64\x64'));
//输出结果 2020-07-04
