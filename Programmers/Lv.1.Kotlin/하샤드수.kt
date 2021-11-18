class Solution {
    fun solution(x: Int): Boolean {
        var answer = x
        var sum = 0
        
        while (answer > 0) {
            sum += answer % 10
            answer /= 10
        }
        
        return x % sum == 0
    }
}