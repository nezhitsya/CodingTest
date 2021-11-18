class Solution {
    fun solution(s: String): String {
        var answer = ""
        
        if (s.length % 2 == 0) {
            answer = s.get((s.length / 2) - 1).toString() + s.get(s.length / 2).toString()
        } else {
            answer = s.get(s.length / 2).toString()
        }
        
        return answer
    }

    // fun solution(s: String): String =
    //     s.slice((s.length - 1) / 2 .. s.length / 2)
}