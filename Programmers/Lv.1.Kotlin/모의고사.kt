class Solution {
    fun solution(answers: IntArray): IntArray {
        var one = intArrayOf(1, 2, 3, 4, 5)
        var two = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5)
        var three = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        var answer = arrayListOf<Int>()
        var (onecnt, twocnt, threecnt) = arrayOf(Pair(0, 1), Pair(0, 2), Pair(0, 3))
        
        for (i in answers.indices) {
            if (answers[i] == one[i % 5]) {
                onecnt = onecnt.copy(first = onecnt.first + 1, second = onecnt.second)
            }
            
            if (answers[i] == two[i % 8]) {
                twocnt = twocnt.copy(first = twocnt.first + 1, second = twocnt.second)
            }
            
            if (answers[i] == three[i % 10]) {
                threecnt = threecnt.copy(first = threecnt.first + 1, second = threecnt.second)
            }
        }
        
        var arr = listOf(onecnt, twocnt, threecnt).sortedByDescending { it.first }
        answer.add(arr[0].second)
        
        if(arr[1].first == arr[0].first)
            answer.add(arr[1].second)
        if(arr[2].first == arr[0].first)
            answer.add(arr[2].second)
            
        return answer.sorted().toIntArray()
    }
}
