var test = require('./test');
var genTest = test.genTest;
var dif = test.dif;
let bubbleSort = function (arr) {
	let swapped = true;
	let len = arr.length;
	//swapped可以提前终止
	do {
		swapped = false;
		for (let i = 1; i < len; i++) {
			if (arr[i - 1] > arr[i]) {
				// js特有的解构赋值交换
				// [arr[i - 1], arr[i]] = [arr[i], arr[i - 1]];
				var temp = arr[i - 1];
				arr[i - 1] = arr[i];
				arr[i] = temp;
				swapped = true;
			}
		}
		//最大的已经到底了
		len--;
	} while (swapped);
	return arr;
}

dif(bubbleSort, 10000);

function bSort(nums) {
	var i, j, temp;
	for (i = 0; i < nums.length - 1; i++)
		for (j = 0; j < nums.length - 1 - i; j++)
			//需要交换
			if (nums[j] > nums[j + 1]) {
				//交换
				temp = nums[j];
				nums[j] = nums[j + 1];
				nums[j + 1] = temp;
			}
	return nums;
}
dif(bSort, 10000);

