fun solution(A: IntArray): Int {
    var result = 0
    
    // xor 연산은 자기 자신과 짝수번 연산하면 0, 홀수번 연산하면 자기 자신으로 도출
    for(i in A.indices) {
        result = result xor A[i]
    }

    return result
}
