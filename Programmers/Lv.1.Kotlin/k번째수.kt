class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = intArrayOf()
        val list = arrayListOf<Int>()

        for(i in commands) {
            val tmp = array.slice(i[0] - 1 until i[1]).sorted()
            list.add(tmp[i[2] - 1])
        }
        
        answer = list.toIntArray()
        return answer
    }

    // fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
    //     return commands.map { command ->
    //         array.slice(IntRange(command[0] - 1, command[1] - 1)).sorted()[command[2] - 1]
    //     }.toIntArray()
    // }
}
