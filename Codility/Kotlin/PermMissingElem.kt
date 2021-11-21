fun solution(A: IntArray): Int {
    if (A.size == 0) return 1
    var sum = 0
    for (i in 1..(A.size + 1)) {
        sum += i
    }
    return sum - A.sum()
}