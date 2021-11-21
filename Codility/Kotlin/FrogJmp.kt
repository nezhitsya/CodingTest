fun soultion(X: Int, Y: Int, D: Int) {
    var count = 0
    var jumpX = X

    while (true) {
        if (jumpX >= Y) {
            break
        }

        jumpX = jumpX + D
        count++
    }

    return count

    // Score 100% 풀이
    if (X > Y || X == Y) return 0
     var k = Y - X
     var answer = k / D

     if ((k % D) > 0) return answer + 1
     else return answer
}