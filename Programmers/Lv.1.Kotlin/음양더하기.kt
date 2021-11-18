class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var answer: Int = 0
        
        for (i in signs.indices) {
            if (signs[i]) answer += absolutes[i]
            else answer -= absolutes[i]
        }
        
        return answer
    }
}