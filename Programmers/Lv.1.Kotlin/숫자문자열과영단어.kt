class Solution {
    fun solution(s: String): Int {
        var answer: String = s
        val nums = mapOf("zero" to "0", "one" to "1", "two" to "2", "three" to "3", "four" to "4", "five" to "5", "six" to "6", "seven" to "7", "eight" to "8", "nine" to "9")
        
        for (n in nums) {
            if(answer.contains(n.key)) {
                answer = answer.replace(n.key, n.value)
            }
        }
        
        return answer.toInt()
    }
}