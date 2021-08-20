function test2(){
	var arrStr = '7|5|1|3|2|4|6'.split('|'), i = 0;
	while (!![]) {
		switch(arrStr[i++]){
			case '1':
				var c = b + 3000;
				continue;
			case '2':
				var e = d + 5000;
				continue;
			case '3':
				var d = c + 4000;
				continue;
			case '4':
				var f = e + 6000;
				continue;
			case '5':
				var b = a + 2000;
				continue;
			case '6':
				return f;
				continue;
			case '7':
				var a = 1000;
				continue;
		}
		break;
	}
}
console.log( test2() );
//输出 21000