class Solution {
    fun solution(scores: Array<IntArray>): String {
        var answer = ""
        var result = 0f
        for (i in scores.indices) {
            var sum = 0
            var cnt = 0
            var max = -1
            var min = 101
            for (j in scores.indices) {
                sum += scores[j][i]
                if (j != i && scores[i][i] == scores[j][i]) {
                    cnt++
                }
                max = Math.max(max, scores[j][i])
                min = Math.min(min, scores[j][i])
            }
            result = if (cnt == 0) {
                if (scores[i][i] == max || scores[i][i] == min) {
                    (sum - scores[i][i]).toFloat() / (scores.size - 1)
                } else {
                    sum.toFloat() / scores.size
                }
            } else {
                sum.toFloat() / scores.size
            }
            answer += if (result >= 90) {
                "A"
            } else if (result >= 80) {
                "B"
            } else if (result >= 70) {
                "C"
            } else if (result >= 50) {
                "D"
            } else "F"
        }
        return answer
    }
}

class Solution {
    fun solution(scores: Array<IntArray>): String {
    return scores.mapIndexed { index, ints ->
        var flag = 0
        var list = arrayListOf<Int>().also { (scores.indices).map { v -> it.add(scores[v][index]) } }
        list.forEach { if (it == ints[index]) flag++ }
        if ((list.max() == ints[index] || list.min() == ints[index]) && flag == 1)
            list.remove(ints[index])
        list.sum() / list.size.toDouble()
    }.joinToString("") {
        when {
            it >= 90 -> "A"
            it >= 80 -> "B"
            it >= 70 -> "C"
            it >= 50 -> "D"
            else -> "F"
        }
    }
}