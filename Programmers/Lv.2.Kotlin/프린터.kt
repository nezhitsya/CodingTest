import java.util.*

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        val waiting: Queue<Pair<Int, Int>> = LinkedList()
        val ready: Queue<Pair<Int, Int>> = LinkedList()
        
        priorities.forEachIndexed { index, priority ->
            waiting.add(index to priority)
        }
        
        while (waiting.isNotEmpty()) {
            if (canPrint(waiting)) {
                ready.add(waiting.poll())
            } else {
                waiting.add(waiting.poll())
            }
        }
        
        return ready.indexOf(ready.filter { it.first == location }.first()) + 1
    }
    
    fun canPrint(q: Queue<Pair<Int, Int>>): Boolean {
        var p = 0
        
        q.forEachIndexed { index, pair ->
            if (index == 0) {
                p = pair.second
            } else {
                if (p < pair.second) return false
            }
        }
        return true
    }

    // fun solution(priorities: IntArray, location: Int): Int {
    //         var printerQueue = ArrayDeque<Pair<Int,Int>>()
    //     priorities.forEachIndexed{index, i ->
    //         printerQueue.offer(Pair(index,i))
    //     }

    //     var count = 0
    //     while (!printerQueue.isEmpty()){
    //         var first = printerQueue.poll()

    //         if(printerQueue.filter { first.second < it.second }.size > 0){
    //             printerQueue.offer(first)
    //         }else{
    //             count++
    //             if(first.first == location) return count
    //         }
    //     }
    //     return 0
    // }
}