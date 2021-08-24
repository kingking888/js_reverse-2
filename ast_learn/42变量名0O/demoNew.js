Date.prototype.format = function (OOOOOO) {
  var OOOOOo = OOOOOO;
  var OOOOO0 = ['日', '一', '二', '三', '四', '五', '六'];
  OOOOOo = OOOOOo.replace(/yyyy|YYYY/, this.getFullYear());
  OOOOOo = OOOOOo.replace(/MM/, this.getMonth() + 1 > 9 ? (this.getMonth() + 1).toString() : '0' + (this.getMonth() + 1));
  OOOOOo = OOOOOo.replace(/dd|DD/, this.getDate() > 9 ? this.getDate().toString() : '0' + this.getDate());
  return OOOOOo;
};

console.log(new Date().format('yyyy-MM-dd')); //输出结果 2020-07-04