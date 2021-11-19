class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer = arrayListOf<Int>()
        
        for (i in 0 until (numbers.size - 1)) {
            for (j in 1 until numbers.size) {
                if (i != j) {
                    answer.add(numbers[i] + numbers[j])
                }
            }
        }
        
        answer.sort()
        return answer.distinct().toIntArray()

        // val list = numbers.toList()

        // return list.withIndex().flatMap { i -> list.withIndex().map { j -> i to j } }
        //     .filter { it.first.index != it.second.index }
        //     .map { it.first.value + it.second.value }
        //     .toSortedSet()
        //     .toIntArray()
    }
}