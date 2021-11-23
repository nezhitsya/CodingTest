import kotlin.math.*

class Solution {
    fun solution(numbers: IntArray, hand: String): String {
        var answer = ""
        var right = 12 // 오른손 위치
        var left = 10 // 왼손 위치
        
        for (num in numbers) {
            if (num == 1 || num == 4 || num == 7) {
                left = num
                answer += "L"
            } else if (num == 3 || num == 6 || num == 9) {
                right = num
                answer += "R"
            } else {
                var location = num
                if (num == 0) location = 11
                if (dis(left, location) < dis(right, location)) {
                    left = location
                    answer += "L"
                } else if (dis(left, location) > dis(right, location)) {
                    right = location
                    answer += "R"
                } else {
                    if (hand == "right") {
                        right = location
                        answer += "R"
                    } else {
                        left = location
                        answer += "L"
                    }
                }
            }
        }
        return answer
    }
    
    // 위아래 차이 3, 양 옆은 차이 1 > 현재 위치 = 눌러야하는 위치 / 3 + 눌러야하는 위치 % 3
    fun dis(number: Int, hand: Int): Int {
        return (abs(number - hand)) % 3 + (abs(number - hand)) / 3
    }
}