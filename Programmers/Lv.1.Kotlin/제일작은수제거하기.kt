class Solution {
    fun solution(arr: IntArray): IntArray = 
        if (arr.size == 1) {
            intArrayOf(-1)
        } else arr.filter {
            it != arr.min()
        }.toIntArray()
    
    // fun solution(arr: IntArray): IntArray {
    //     val answer = arrayListOf<Int>()
    //     var minVal = arr[0]

    //     for (value in arr) {
    //         answer.add(value)

    //         if (minVal > value) {
    //             minVal = value
    //         }
    //     }

    //     answer.remove(minVal)

    //     if (answer.size == 0) {
    //         answer.add(-1)
    //     }

    //     return answer.toIntArray()
    // }
}