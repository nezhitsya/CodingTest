import Foundation

func solution(_ a: Int, _ b: Int) -> String {
  let days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
  let month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  var day = 5   // 16년 1월 1일은 금요일이기 때문
  
  for i in 0..<a-1 {
    day += month[i]
  }
  
  day += b - 1
  return days[day % 7]
}
