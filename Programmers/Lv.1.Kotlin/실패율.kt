class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = arrayListOf<Int>()
        val faillist = arrayListOf<Pair<Int,Float>>() //스테이지 실패율
        var player = stages.size
        
        for(i in 1..N) {
            var cnt = 0
            
            for(j in stages.indices){
                if(stages[j] == i) cnt++
            }
            
            faillist.add(Pair(i, cnt / player.toFloat()))
            player -= cnt
        }
        
        val comparator = compareBy<Pair<Int,Float>> { -it.second }
        val secondcomp = comparator.thenBy { it.first }
        faillist.sortWith(secondcomp)
        
        for(i in faillist.indices) {
            answer.add(faillist[i].first)
        }
        
        return answer.toIntArray()
    }
}