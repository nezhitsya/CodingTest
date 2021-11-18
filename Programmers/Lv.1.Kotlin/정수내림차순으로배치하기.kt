class Solution {
    fun solution(n: Long): Long {
        return n.toString().map {
            it.toString().toInt()
        }.sortedDescending().joinToString("").toLong()
    }

    // fun solution(n: Long): Long = String(n.toString().toCharArray().sortedArrayDescending()).toLong()
}