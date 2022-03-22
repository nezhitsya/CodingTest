import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var cloth = Array(repeating: 0, count: n)
    
    for i in lost { cloth[i - 1] = -1 }
    for j in reserve { cloth[j - 1] = 1 }
    for (idx, v) in cloth.enumerated() {
        if v == -1 {
            if idx > 0 && cloth[idx - 1] == 1 {
                cloth[idx] += 1
                cloth[idx - 1] -= 1
            } else if idx < cloth.count - 1 && cloth[idx + 1] == 1 {
                cloth[idx] += 1
                cloth[idx + 1] -= 1
            }
        }
    }
    
    return cloth.filter{ $0 >= 0 }.count
}
