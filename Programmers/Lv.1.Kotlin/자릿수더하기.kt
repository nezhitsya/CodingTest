class Solution {
    fun solution(n: Int): Int {
        return n.toString().map {
            it.toInt() - '0'.toInt()
        }.sum()
    }

    // fun solution(n: Int): Int {
    //     var input = n
    //     var answer = 0

    //     while (input != 0) {
    //         answer += input % 10
    //         input /= 10
    //     }

    //     return answer
    // }
}