// 완전탐색
import kotlin.math.*

class Solution {
    lateinit var visited: BooleanArray
    lateinit var dungeonsArr: Array<IntArray>
    var num: Int = 0
    
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        visited = BooleanArray(dungeons.size)
        dungeonsArr = dungeons
        
        for (i in 0 until dungeons.size) {
            visited[i] = false
        }
        
        search(0, k)
        return num
    }
    
    fun search(count: Int, k: Int) {
        for (i in 0 until dungeonsArr.size) {
            var temp = k
            
            if (temp >= dungeonsArr[i][0] && !visited[i]) {
                temp -= dungeonsArr[i][1]
                
                visited[i] = true
                search(count + 1, temp)
                visited[i] = false
            }
        }
        num = max(num, count)
    }
}