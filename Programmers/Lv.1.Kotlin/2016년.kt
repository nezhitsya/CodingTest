class Solution {
    fun solution(a: Int, b: Int): String {
        var month = listOf(31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        var day = listOf("THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED")
        var dday = (0 until a - 1).map {
            month[it]
        }.sum() + b
        
        return day[dday % 7]
    }
}