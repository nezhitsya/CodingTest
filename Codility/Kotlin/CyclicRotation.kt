fun solution(A: IntArray, K: Int): IntArray {
    // A 리스트 크기의 리스트 생성
    var alist = IntArray(A.size)

    // A 리스트 탐색
    for (i in A.indices) {
        if (A.size == 0) {
            alist = A
        }

        // i + K가 A 길이를 넘을 경우 맨 앞에서 넘는 길이 만큼 인덱스 이동
        if ((i + K) >= A.size) {
            alist[i + K - A.size] = A[i]
        // i + K가 A 길이를 넘지 않을 경우 K만큼 인덱스 이동
        } else {
            alist[i + K] = A[i]
        }

        // Score 100% 풀이
        // alist[(i + K) % A.size] = A[i]
    }

    return alist
}