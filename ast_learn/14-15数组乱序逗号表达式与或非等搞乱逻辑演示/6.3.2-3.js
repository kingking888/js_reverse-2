function test2(a, b, c, d, e, f){
	return f = (e = (d = (c = (b = (a = 1000, a + 50, b + 60, c + 70, a + 2000), d + 80, b + 3000), e + 90, c + 4000), f + 100 ,d + 5000), e + 6000);
}
console.log( test2() );
// 输出 21000