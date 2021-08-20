Date.prototype.format = function (formatStr) {
  var str = formatStr;
  var Week = [atob("5Q=="), atob("AA=="), atob("jA=="), atob("CQ=="), atob("2w=="), atob("lA=="), atob("bQ==")];
  str = str.replace(/yyyy|YYYY/, this.getFullYear());
  str = str.replace(/MM/, this.getMonth() + 1 > 9 ? (this.getMonth() + 1).toString() : atob("MA==") + (this.getMonth() + 1));
  str = str.replace(/dd|DD/, this.getDate() > 9 ? this.getDate().toString() : atob("MA==") + this.getDate());
  return str;
};

console.log(new Date().format(atob("eXl5eS1NTS1kZA=="))); //输出结果 2020-07-04