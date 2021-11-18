class Solution {
    fun solution(s: String): Boolean {
        return s.all {
            it.isDigit()
        } && ((s.length == 4 || s.length == 6))

        // val length = s.filter { it.isDigit() }.length
        // return (length == 4 || length == 6) && length == s.length
    }
}