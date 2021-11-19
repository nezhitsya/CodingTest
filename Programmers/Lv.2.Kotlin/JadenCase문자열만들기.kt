class Solution {
    fun solution(s: String): String {
        var answer = ""
        var list = s.split(" ")
        
        for (i in list.indices) {
            for (j in list[i].indices) {
                answer += if (j == 0) list[i][j].toUpperCase()
                            else list[i][j].toLowerCase()
            }
            if (i != list.size - 1) {
                answer += " "
            }
        }
        
        return answer
    }

    // fun solution(s: String): String {
    //       return s.toLowerCase().split(" ").map {
    //             it.capitalize()
    //         }.joinToString(" ")
    // }
}

fun main() {
    val s = Solution()
    println(s.solution("3people unFollowed me"))
    println(s.solution("for the last week"))
    println(s.solution("1234 gggg"))
    println(s.solution("AAAAAAA"))
    println(s.solution("Hello World"))
    println(s.solution("Hello  World"))
    println(s.solution("Hello world "))
}