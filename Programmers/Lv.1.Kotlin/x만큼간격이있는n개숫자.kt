class Solution {
    fun solution(x: Int, n: Int): LongArray {
        var answer = LongArray(n)

        for (i in 1..n) {
            answer[i - 1] = i * x.toLong()
        }

        return answer
    }

    // fun solution(x: Int, n: Int): LongArray = LongArray(n) {
    //     x.toLong() * (it + 1) 
    // }
}