class Solution {
    fun solution(seoul: Array<String>): String {
        var location = seoul.indexOf("Kim")
        return "김서방은 ${location}에 있다"
    }

    // fun solution(seoul: Array<String>): String = "김서방은 ${seoul.indexOf("Kim")}에 있다"
}