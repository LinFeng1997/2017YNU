// 自定义测试用例
/**
 * 
 * 
 * @param {any} n 元素个数
 * @param {any} rangeL  范围内最小数，开区间 
 * @param {any} rangeH  范围内最大数，开区间
 * @returns arr 数组
 */
function genTest(n, rangeL, rangeH) {
    if (rangeH < rangeL) {
        return;
    }
    var arr = [];
    for (var i = 0; i < n; i++) {
        arr.push(Math.floor(Math.random() * (rangeH - rangeL)) + rangeL);
    }
    return arr;
}

// 耗时计算
/**
 * 
 * 
 * @param {any} func 要测试的回调函数
 * @param {any} n 元素个数
 * @param {any} [m=n] 最大值，默认为n
 */
function dif(func,n,m=n) {
    console.time(`${func.name}算法耗时`);
    func(genTest(n, 0, m));
    console.timeEnd(`${func.name}算法耗时`);    
}

exports.genTest = genTest;
exports.dif = dif;
