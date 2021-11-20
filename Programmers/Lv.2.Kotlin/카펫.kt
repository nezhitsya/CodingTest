class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        var answer = intArrayOf()
        val yellowSize = getCombination(yellow).filter {
            // brown 면적 = (yellow 가로 + 2) * (yellow 세로 + 2) - (yellow 가로) * (yellow 세로)
            (it.first + 2) * (it.second + 2) - it.first * it.second == brown
        }.first()
        
        return intArrayOf(yellowSize.first + 2, yellowSize.second + 2)
    }
    
    fun getCombination(number:Int): MutableList<Pair<Int, Int>> {
        if (number == 1) return mutableListOf(1 to 1)
        
        val result = mutableListOf<Pair<Int, Int>>()
        for (i in (1..(number / 2))) {
            if (number % i ==0) result.add(number / i to i)
        }
        
        return result
    }

    // fun solution(brown: Int, yellow: Int): IntArray {
    //     return (1..yellow)
    //             .filter { yellow % it == 0 }
    //             .find { lineCount -> brown == (lineCount * 2) + ((yellow / lineCount + 2) * 2) }
    //             .let { intArrayOf((yellow / it!!) + 2, it + 2) }
    // }
}