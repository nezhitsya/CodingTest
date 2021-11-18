import kotlin.math.*

class Solution {
    fun solution(nums: IntArray): Int {
        var answer = 0
 
        for (i in 0 until nums.size - 2) {
            for (j in (i + 1) until nums.size - 1) {
                for (k in (j + 1) until nums.size) {
                    if (isPrime(nums[i] + nums[j] + nums[k])) {
                        answer++
                    }
                }
            }
        }

        return answer
    }
    
    fun isPrime(n: Int): Boolean {
        if (n == 1) return false
        
        for (i in 2..sqrt(n.toDouble()).toInt()) {
            if (n % i == 0) return false
        }
        
        return true
    }
}