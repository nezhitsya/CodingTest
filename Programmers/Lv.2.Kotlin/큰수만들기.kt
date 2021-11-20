import java.util.*

class Solution {
    fun solution(number: String, k: Int): String {
        var answer = Stack<Char>()
        var del = k
        
        number.forEach {
            // stack이 비지않고, 맨 위 값이 작고, 남은 삭제 횟수가 0 이상일 때
            while (answer.isNotEmpty() && answer.peek() < it && del > 0) {
                answer.pop()
                del--
            }
            answer.push(it)
        }
        
        for (i in 1..del) answer.pop()
        
        return answer.toArray().joinToString("")
    }
}