class Solution {
    fun solution(left: Int, right: Int): Int {
        var answer: Int = 0
        
        for (i in left..right) {
            if (count(i) % 2 == 0) answer += i
            else answer -= i
        }
        
        return answer
    }
    
    fun count(n: Int): Int {
        var nums: Int =0
        
        for (i in 1..n) {
            if (n % i == 0) nums++
        }
        
        return nums
    }

    // fun solution(left: Int, right: Int): Int {
    //     return (left..right).map { i -> if ((1..i).filter { i % it == 0 }.size % 2 == 0) i else -i }.sum()
    // }
}