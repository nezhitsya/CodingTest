import kotlin.math.*

class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = arrayListOf<Int>()
        var available = progresses.mapIndexed { index, already ->
            ceil((100 - already).toDouble().div(speeds.get(index)))
        }
        var deploy = available.first()
        var count = 0
        
        available.forEach {
            if (deploy < it) {
                deploy = it
                answer.add(count)
                count = 0
            }
            count++
        }
        answer.add(count)
        
        return answer.toIntArray()
    }
}