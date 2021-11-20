class Solution {
    lateinit var answer: MutableSet<Int>
    
    fun solution(numbers: String): Int {
        answer = mutableSetOf()
        getCombination(numbers, "")
        return answer.filter { isPrime(it) }.count()
    }
    
    fun getCombination(numbers: String, result: String) {
        if (result.isNotEmpty()) answer.add(result.toInt())
        if (numbers.isEmpty()) return
        
        numbers.forEachIndexed { index, c ->
            getCombination(numbers.removeRange(index..index), c.plus(result))
        }
    }
    
    fun isPrime(number: Int): Boolean {
        if (number == 1 || number == 0) {
            return false
        }
        
        for (i in (2..(number / 2))) {
            if (number % i == 0) {
                return false
            }
        }
        
        return true
    }
}