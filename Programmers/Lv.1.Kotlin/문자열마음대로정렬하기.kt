class Solution {
    fun solution(strings: Array<String>, n: Int): Array<String> {
        //객체의 속성을 전혀 사용하지 않거나 변경하지 않고 사용하는 경우에 also
        return strings.also {
            it.sort()
            it.sortBy { it[n] }
        }
    }
}