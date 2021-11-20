class Solution {
    fun solution(citations: IntArray): Int = citations.sortedDescending().filterIndexed { index, i ->
        (index + 1) <= i
    }.lastIndex + 1

    // fun solution(citations: IntArray): Int {
    //     val result = citations.sortedArrayDescending()

    //     for (i in 0 until result.size) {
    //         if (result[i] < i + 1) {
    //             return i
    //         }
    //     }

    //     return citations.size
    // }
}