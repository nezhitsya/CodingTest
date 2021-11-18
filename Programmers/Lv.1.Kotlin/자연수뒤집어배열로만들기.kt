class Solution {
    fun solution(n: Long): IntArray {
        return n.toString().reversed().map {
            it.toString().toInt()
        }.toIntArray()

        // var num = n
        // var answer = intArrayOf()

        // while(num > 0) {
        //     answer = answer + (num % 10).toInt()
        //     num = num / 10
        // }

        // return answer
    }
}