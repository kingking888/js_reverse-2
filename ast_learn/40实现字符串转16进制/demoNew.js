var arr = ["jA==", "CQ==", "2w==", "lA==", "bQ==", "MA==", "eXl5eS1NTS1kZA==", "5Q==", "AA=="];

(function (myArr, num) {
  var xiaojianbang = function (nums) {
    while (--nums) {
      myArr["\\u0070\\u0075\\u0073\\u0068"](myArr["\\u0073\\u0068\\u0069\\u0066\\u0074"]());
    }
  };

  xiaojianbang(++num);
})(arr, 0x10);

Date.prototype.format = function (formatStr) {
  var str = formatStr;
  var Week = [atob(arr[0]), atob(arr[1]), atob(arr[2]), atob(arr[3]), atob(arr[4]), atob(arr[5]), atob(arr[6])];
  str = str.replace(/yyyy|YYYY/, this.getFullYear());
  str = str.replace(/MM/, this.getMonth() + 1 > 9 ? (this.getMonth() + 1).toString() : atob(arr[7]) + (this.getMonth() + 1));
  str = str.replace(/dd|DD/, this.getDate() > 9 ? this.getDate().toString() : atob(arr[7]) + this.getDate());
  return str;
};

console.log(new Date().format(atob(arr[8]))); //输出结果 2020-07-04