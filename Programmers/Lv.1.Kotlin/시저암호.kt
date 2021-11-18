class Solution {
    fun solution(s: String, n: Int): String {
        return s.toList().joinToString("") {
            when (it) {
                in 'A'..'Z' ->
                    ('A'.toInt() + (it.toInt() - 'A'.toInt() + n) % ('Z' - 'A' + 1)).toChar()
                in 'a'..'z' ->
                    ('a'.toInt() + (it.toInt() - 'a'.toInt() + n) % ('z' - 'a' + 1)).toChar()
                else -> it
            }.toString()
        }
    }
}

// class Solution {
//     fun solution(s: String, n: Int): String {
//         var answer = ""

//         for(c in s) {
//             if(c == ' ') {
//                 answer += ' '
//             } else {
//                 answer += getAlphabet(c, n)   
//             }
//         }
//         return answer
//     }

//     fun getAlphabet(c: Char, n: Int): Char {
//         var isUpper = false
//         var ascii = c.toInt()
//         if(ascii >= 65 && ascii <= 90) isUpper = true
//         ascii += n
//         if(isUpper) {
//             if(ascii > 90) ascii = ascii - 90 + 65 - 1
//         } else {
//             if(ascii > 122) ascii = ascii - 122 + 97 - 1
//         }

//         return ascii.toChar()
//     }
// }
