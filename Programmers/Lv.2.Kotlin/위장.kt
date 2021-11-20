class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        val cody = mutableMapOf<String, Int>()
        
        clothes.forEach {
            val count = cody.get(it.get(1)) ?: 0
            cody.put(it.get(1), count + 1)
        }
        
        return cody.map { it.value + 1 }.reduce { acc, i -> acc * i } - 1

        // return clothes.groupBy { it[1] }.values.fold(1) { acc, i -> acc * (i.size + 1) } - 1
    }
}