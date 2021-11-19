class Solution {
    fun solution(arr: IntArray): Int {
        var answer = arr[0]
        for(i in 1 until arr.size)
            answer = lcm(answer, arr[i])
        return answer
    }

    fun gcd(a: Int, b: Int): Int {
        if (b == 0)
            return a
        return gcd(b, a % b)
    }

    fun lcm(a: Int, b: Int): Int {
        return a * b / gcd(a, b)
    }

    // fun solution(arr: IntArray): Int {
    //     var answer = 1
    //     while (true) {
    //         var x = 0
    //         for (a in arr) x += answer % a
    //         if (x == 0) return answer
    //         answer++
    //     }
    //     return answer
    // }
}

fun main() {
    val s = Solution()
    println(s.solution(intArrayOf(2, 6, 8, 14)))
    println(s.solution(intArrayOf(1, 2, 3)))
}