class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        var answer = arrayOf<IntArray>()

        // arr1의 인덱스와 해당 인덱스 배열
        answer = arr1.mapIndexed { indexArr, nums ->
            // arr1의 각 배열의 인덱스와 값
            nums.mapIndexed {indexNums, i ->
                i + arr2[indexArr][indexNums]
            }.toIntArray()
        }.toTypedArray()

        return answer

        // return Array(arr1.size) { row ->
        //     IntArray(arr1[0].size) { col ->
        //         arr1[row][col] + arr2[row][col]
        //     }
        // }
    }
}