class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        var answer: IntArray = intArrayOf(0, 0)
        var count = 0
        var num = 0
        
        for (i in lottos.indices) {
            if (lottos[i] == 0) {
                count++
            } else {
                if (win_nums.contains(lottos[i])) {
                    num++
                }
            }
        }
        
        answer[0] = checkNum(num + count)
        answer[1] = checkNum(num)
        
        return answer
    }
    
    fun checkNum(lotto: Int): Int {
        if (lotto == 6) {
            return 1
        } else if (lotto == 5) {
            return 2
        } else if (lotto == 4) {
            return 3
        } else if (lotto == 3) {
            return 4
        } else if (lotto == 2) {
            return 5
        } else {
            return 6
        }
    }

    // fun solution(lottos: IntArray, winNums: IntArray): IntArray {
    //     return intArrayOf(
    //             (lottos.size.plus(1)) - lottos.filter { winNums.contains(it) || it == 0 }.size,
    //             (lottos.size.plus(1)) - lottos.filter(winNums::contains).size
    //     ).map { if (it > 6) it - 1 else it }.toIntArray()
    // }
}