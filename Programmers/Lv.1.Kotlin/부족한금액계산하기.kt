import kotlin.math.*

class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        var answer: Long = 0L
        
        for (i in 1..count) {
            answer += price * i
        }
        
        return max(0, money - answer)
    }

    // fun solution(price: Int, money: Int, count: Int): Long = (1..count).map { 
    //     it * price.toLong()
    // }.sum().let {
    //     if (money > it) 0 else it - money
    // }
}