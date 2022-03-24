import Foundation

func solution(_ s:String) -> String {
    let index = s.count / 2
    let isEven = s.count % 2 == 0
    
    if isEven {
        let startIndex = s.index(s.startIndex, offsetBy: index - 1)
        let endIndex = s.index(s.startIndex, offsetBy: index)
        
        return String(s[startIndex...endIndex])
    } else {
        let startIndex = s.index(s.startIndex, offsetBy: index)
        let endIndex = s.index(s.startIndex, offsetBy: index)
        
        return String(s[startIndex...endIndex])
    }
    
}
