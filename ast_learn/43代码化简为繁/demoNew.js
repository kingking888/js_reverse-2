Date.prototype.format = function (formatStr) {
  function _xxx7(a, b) {
    return a + b;
  }

  function _xxx6(a, b) {
    return a > b;
  }

  function _xxx5(a, b) {
    return a + b;
  }

  function _xxx4(a, b) {
    return a + b;
  }

  function _xxx3(a, b) {
    return a + b;
  }

  function _xxx2(a, b) {
    return a + b;
  }

  function _xxx(a, b) {
    return a > b;
  }

  var str = formatStr;
  var Week = ['日', '一', '二', '三', '四', '五', '六'];
  str = str.replace(/yyyy|YYYY/, this.getFullYear());
  str = str.replace(/MM/, _xxx(_xxx2(this.getMonth(), 1), 9) ? _xxx3(this.getMonth(), 1).toString() : _xxx4('0', _xxx5(this.getMonth(), 1)));
  str = str.replace(/dd|DD/, _xxx6(this.getDate(), 9) ? this.getDate().toString() : _xxx7('0', this.getDate()));
  return str;
};

console.log(new Date().format('yyyy-MM-dd')); //输出结果 2020-07-04