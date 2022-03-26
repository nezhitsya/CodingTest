import Foundation

func solution(_ nums:[Int]) -> Int {
   let numsArr = nums.sorted()
   var sosuNums = [Int]()
   var count = 0

   for i in 0 ... numsArr.count - 3 {
      for j in i + 1 ... numsArr.count - 2 {
         for k in j + 1 ... numsArr.count - 1 {
            sosuNums.append(numsArr[i] + numsArr[j] + numsArr[k])
         }
      }
   }

   sosuNums.forEach { (num) in
      var isSosu = true
      for n in 2 ..< num {
         if num % n == 0 { isSosu = false }
      }
      if isSosu { count += 1}
   }

   return count
}
