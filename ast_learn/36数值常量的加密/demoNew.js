Date.prototype.format = function (formatStr) {
  var str = formatStr;
  var Week = ['日', '一', '二', '三', '四', '五', '六'];
  str = str.replace(/yyyy|YYYY/, this.getFullYear());
  str = str.replace(/MM/, this.getMonth() + (424685 ^ 424684) > (318588 ^ 318581) ? (this.getMonth() + (216490 ^ 216491)).toString() : '0' + (this.getMonth() + (424794 ^ 424795)));
  str = str.replace(/dd|DD/, this.getDate() > (305097 ^ 305088) ? this.getDate().toString() : '0' + this.getDate());
  return str;
};

console.log(new Date().format('yyyy-MM-dd')); //输出结果 2020-07-04