import java.util.*

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        if (truck_weights.size == 0) return 0
        
        var answer = 0
        val trucks: Queue<Int> = LinkedList()
        trucks.addAll(truck_weights.map { it })
        val bridge: Queue<Int> = LinkedList()
        bridge.addAll(IntArray(bridge_length, { 0 }).toList())
        
        while (trucks.isNotEmpty()) {
            bridge.poll()
            if (bridge.sum() + trucks.peek() <= weight) {
                bridge.add(trucks.poll())
            } else {
                bridge.add(0)
            }
            answer++
        }
        
        return answer + bridge_length
    }
}