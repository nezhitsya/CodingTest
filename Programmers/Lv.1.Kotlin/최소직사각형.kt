import kotlin.math.*

class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        var arr = sizes.mapIndexed { indexArr, items ->
            if (items[0] < items[1]) {
                var temp = items[0]
                items[0] = items[1]
                items[1] = temp
            }
        }.toTypedArray()
        
        var maxX = 0
        var maxY = 0
        
        for (i in 0..sizes.size - 1) {
            maxX = max(sizes[i][0], maxX)
            maxY = max(sizes[i][1], maxY)
        }
        
        return maxX * maxY
    }

    // fun solution(sizes: Array<IntArray>): Int {
    //     var a = 0
    //     var b = 0

    //     for (array in sizes) {
    //         array.sort()
    //         if (array.isNotEmpty()) {
    //             a = array.first().coerceAtLeast(a)
    //             b = array.last().coerceAtLeast(b)
    //         }
    //     }
    //     return a * b
    // }
}