class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        var answer = Array<IntArray>(arr1.size) { IntArray(arr2.first().size){ 0 } }
        
        for (row in arr1.indices) {
            for (col2 in arr2.first().indices) {
                for (col in arr1[row].indices) {
                    answer[row][col2] += arr1[row][col] * arr2[col][col2]
                }
            }
        }
        
        return answer
    }
}