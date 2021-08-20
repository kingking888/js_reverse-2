var bigArr = [
    true,
    'xiaojianbang',
    1000,
    [100, 200, 300], {
        name: 'xiaojianbang',
        money: 0
    },
    function () {
        console.log('Hello')
    }
];
console.log(bigArr[0]);			//true
console.log(bigArr[1]);			//xiaojianbang
console.log(bigArr[2]);			//1000
console.log(bigArr[3][0]);		//100
console.log(bigArr[4].money);	//0
console.log(bigArr[5]());		//Hello
