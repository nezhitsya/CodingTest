fun solution(N: Int): Int {
    var binary = N.toString(2) // 2 진법 String
    var gap: Int = 0 // 1과 1사이 0 개수
    var gaps = arrayListOf<Int>() // 1과 1사이 0 개수 리스트
    var maximum = 0 // 0 개수 최댓값

    // 2 진법 String에서 각 Char 비교
    for (i in binary) {
        // 1이 나온 경우, 0 개수 리스트에 저장 및 개수 0으로 초기화
        if (i == '1') {
            gaps.add(gap)
            gap = 0
        // 0이 나온 경우, 0 개수 1 추가
        } else {
            gap += 1
        }
    }

    // 0 개수 리스트 탐색하여 가장 큰 값 도출
    for (i in gaps) {
        if (i > maximum) {
            maximum = i
        }
    }

    return maximum
}
