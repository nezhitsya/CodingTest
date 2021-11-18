class Solution {
    fun solution(phone_number: String): String {
        var answer = arrayListOf<String>()
        
        for (i in phone_number.indices) {
            if (i < phone_number.length - 4) {
                answer.add("*")
            } else {
                answer.add(phone_number[i].toString())
            }
        }
        
        return answer.joinToString("")

        // return phone_number.mapIndexed { index, c ->
        //     if (phone_number.length - 5 < index) c else "*"
        // }.joinToString("")
    }
}