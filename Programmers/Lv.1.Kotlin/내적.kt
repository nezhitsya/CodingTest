class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        var answer: Int = 0
        
        for (i in a.indices) {
            answer += a[i] * b[i]
        }
        
        return answer

        // return a.zip(b).map { it.first * it.second }.sum()
    }

    // fun solution(a: IntArray, b: IntArray): Int = a.mapIndexed { index, it -> it * b[index] }.sum()
}