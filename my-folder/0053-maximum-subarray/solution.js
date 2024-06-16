/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSum =  nums[0];
    let curSum = 0

    for ( let n of nums) {
        if (curSum <0) {
            curSum = 0
        }
        curSum += n
        maxSum = Math.max(maxSum,curSum)
    }
    return maxSum
};
