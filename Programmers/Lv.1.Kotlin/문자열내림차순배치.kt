class Solution {
    fun solution(s: String): String = String(s.toCharArray().sortedArrayDescending())
}

// class Solution {
//     fun solution(s: String): String {
//          val array = s.toCharArray()

//             for(i in 0 until array.size){
//                 for (j in i until array.size) {
//                     if (array[i] < array[j]) {
//                         val temp = array[i]
//                         array[i] = array[j]
//                         array[j] = temp
//                     } 
//                 }
//             }

//             return String(array)
//     }
// }
