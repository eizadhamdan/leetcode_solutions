/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    const ans = [];
    const sol = [];
    backtrack(1, n, k, sol, ans);
    return ans;
};

function backtrack(start, n, k, sol, ans) {
    if (sol.length === k) {
        ans.push([...sol]);
        return;
    }

    for (let i = start; i <= n; i++) {
        sol.push(i);
        backtrack(i + 1, n, k, sol, ans);
        sol.pop();
    }
}