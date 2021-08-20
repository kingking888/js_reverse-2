Date.prototype.\u0066\u006f\u0072\u006d\u0061\u0074 = function(formatStr) {
    var \u0073\u0074\u0072 = \u0066\u006f\u0072\u006d\u0061\u0074\u0053\u0074\u0072;
    var Week = ['\u65e5', '\u4e00', '\u4e8c', '\u4e09', '\u56db', '\u4e94', '\u516d'];
    str = str['replace'](/yyyy|YYYY/, this['getFullYear']());
    str = str['replace'](/MM/, (this['getMonth']() + 1) > 9 ? (this['getMonth']() + 1)['toString']() : '0' + (this['getMonth']() + 1));
    str = str['replace'](/dd|DD/, this['getDate']() > 9 ? this['getDate']()['toString']() : '0' + this['getDate']());
    return str;
}
console.log( new \u0077\u0069\u006e\u0064\u006f\u0077['\u0044\u0061\u0074\u0065']()['format']('\x79\x79\x79\x79\x2d\x4d\x4d\x2d\x64\x64') );
//输出结果 2020-07-04