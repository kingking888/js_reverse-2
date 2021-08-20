function hello(n) {
  console.log(n);
}

let obj = {
  name: 'xiaojianbang',
  // 这是干啥
  add: function (a, b) {
    "Before";
    return a + b + 1000;
    "After";
  },
  mul: function (a, b) {
    "Before";
    return a * b + 1000;
    "After";
  }
};