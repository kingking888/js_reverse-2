Date.prototype.format = function (_0x2ba6ea0) {
  var _0x2ba6ea1 = _0x2ba6ea0;
  var _0x2ba6ea2 = ['日', '一', '二', '三', '四', '五', '六'];
  _0x2ba6ea1 = _0x2ba6ea1.replace(/yyyy|YYYY/, this.getFullYear());
  _0x2ba6ea1 = _0x2ba6ea1.replace(/MM/, this.getMonth() + 1 > 9 ? (this.getMonth() + 1).toString() : '0' + (this.getMonth() + 1));
  _0x2ba6ea1 = _0x2ba6ea1.replace(/dd|DD/, this.getDate() > 9 ? this.getDate().toString() : '0' + this.getDate());
  return _0x2ba6ea1;
};

console.log(new Date().format('yyyy-MM-dd')); //输出结果 2020-07-04