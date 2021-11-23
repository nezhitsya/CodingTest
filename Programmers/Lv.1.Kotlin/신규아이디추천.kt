class Solution {
    fun solution(new_id: String): String {
        var answer: String = new_id
        val reg1 = Regex("[a-z0-9-_.]")
        val reg2 = Regex("[.]{2,}")
        
        answer = answer.toLowerCase()
        var temp = StringBuilder()
        
        for (c in answer) {
            if (reg1.containsMatchIn(c.toString())) {
                temp.append(c)
            }
        }
        
        answer = temp.toString().replace(reg2, ".")
        
        if (answer.isNotEmpty() && answer.first() == '.') {
            answer = answer.removeRange(0, 1)
        }
        if (answer.isNotEmpty() && answer.last() == '.') {
            answer = answer.removeRange(answer.length - 1, answer.length)
        }
        
        if (answer.isEmpty()) {
            answer = "a"
        }
        
        if (answer.length >= 16) {
            answer = answer.slice(0..14)
        }
        
        if (answer.isNotEmpty() && answer.first() == '.') {
            answer = answer.removeRange(0, 1)
        }
        if (answer.isNotEmpty() && answer.last() == '.') {
            answer = answer.removeRange(answer.length - 1, answer.length)
        }
        
        while (answer.length <= 2) {
            answer += answer[answer.length - 1]
        }
        
        return answer
    }

    // fun solution(newId: String) = newId.toLowerCase()
    //     .filter { it.isLowerCase() || it.isDigit() || it == '-' || it == '_' || it == '.' }
    //     .replace("[.]*[.]".toRegex(), ".")
    //     .removePrefix(".").removeSuffix(".")
    //     .let { if (it.isEmpty()) "a" else it }
    //     .let { if (it.length > 15) it.substring(0 until 15) else it }.removeSuffix(".")
    //     .let {
    //         if (it.length <= 2)
    //             StringBuilder(it).run {
    //                 while (length < 3) append(it.last())
    //                 toString()
    //             }
    //         else it }
}