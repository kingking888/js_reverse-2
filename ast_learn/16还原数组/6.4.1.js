eval(function (p, a, c, k, e, r) {
    e = function (c) {
        return c.toString(36)
    };
    if ('0'.replace(0, e) == 0) {
        while (c--)
            r[e(c)] = k[c];
        k = [function (e) {
                return r[e] || e
            }
        ];
        e = function () {
            return '[2-8a-f]'
        };
        c = 1
    };
    while (c--)
        if (k[c])
            p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
    return p
}('7.prototype.8=function(a){b 2=a;b Week=[\'日\',\'一\',\'二\',\'三\',\'四\',\'五\',\'六\'];2=2.4(/c|YYYY/,3.getFullYear());2=2.4(/d/,(3.5()+1)>9?(3.5()+1).e():\'0\'+(3.5()+1));2=2.4(/f|DD/,3.6()>9?3.6().e():\'0\'+3.6());return 2};console.log(new 7().8(\'c-d-f\'));', [], 16, '||str|this|replace|getMonth|getDate|Date|format||formatStr|var|yyyy|MM|toString|dd'.split('|'), 0, {}))
