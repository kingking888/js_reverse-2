var obj = {
	name: 'xiaojianbang',
	add: function(a, b){
		return a + b;
	}
}
function sub(a, b){
	return a - b;
}
function test() {
    return c = (b = (a = 1000, sub)(a, 3000) + 1, b + (0, obj).add(b, 2000)),
    c + (0, obj).name;
}