function test1(){
	var a, b, c, d, e, f;
	return a = 1000,
	b = a + 2000,
	c = b + 3000,
	d = c + 4000,
	e = d + 5000,
	f = e + 6000,
	f
}
console.log( test1() );
//输出 21000