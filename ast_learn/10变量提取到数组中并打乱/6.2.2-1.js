var bigArr = [
	'\u65e5', '\u4e00', '\u4e8c', '\u4e09', '\u56db', '\u4e94', 
	'\u516d', 'cmVwbGFjZQ==', 'Z2V0TW9udGg=', 'dG9TdHJpbmc=', 
	'Z2V0RGF0ZQ==', 'MA==', ""['constructor']['fromCharCode']
];
(function(arr, num){
	var shuffer = function(nums){
		while(--nums){
			arr.unshift(arr.pop());
		}
	};
	shuffer(++num);
}(bigArr, 0x20));
console.log( bigArr );
//["cmVwbGFjZQ==", "Z2V0TW9udGg=", "dG9TdHJpbmc=", "Z2V0RGF0ZQ==", "MA==", f, "日", "一", "二", "三", "四", "五", "六"]
//console.log( bigArr[5](120) );     //输出 x