class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var answer = 0
        var arr = Array(n + 1) { 1 }
        
        for (i in lost.indices) { arr[lost[i]]-- }
        for (i in reserve.indices) { arr[reserve[i]]++ }
        for (i in 1..n) {
            if (arr[i] == 0) {
                if (arr[i - 1] == 2) {
                    arr[i - 1]--
                    arr[i] = 1
                } else if (i + 1 <= n) {
                    if (arr[i + 1] == 2) {
                        arr[i + 1]--
                        arr[i] = 1
                    }
                }
            }
        }
        
        for (i in 1..n) {
            if (arr[i] > 0) answer++
        }
        
        return answer
    }

    // fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
    //     var answer = n
    //     var lostSet = lost.toSet() - reserve.toSet()
    //     var reserveSet = (reserve.toSet() - lost.toSet()) as MutableSet

    //     for (i in lostSet) {
    //         when {
    //             i + 1 in reserveSet -> reserveSet.remove(i + 1)
    //             i - 1 in reserveSet -> reserveSet.remove(i - 1)
    //             else -> answer--
    //         }
    //     }
    //     return answer
    // }
}