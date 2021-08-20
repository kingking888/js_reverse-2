var obj = {
	name: 'xiaojianbang',
	add: function(a, b){
		return a + b;
	}
}
function sub(a, b){
	return a - b;
}
function test(){
	var a = 1000;
	var b = sub(a,3000) + 1;
	var c = b + obj.add(b, 2000);
	return c + obj.name
}