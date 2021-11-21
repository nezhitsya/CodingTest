import java.util.*

class Solution {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0
        var stack = Stack<Int>()

        moves.forEach {
            for (i in board.indices) {
                if (board[i][it - 1] != 0) {
                    if (stack.isNotEmpty() && stack.peek() == board[i][it - 1]) {
                        answer += 2
                        stack.pop()
                    } else {
                        stack.push(board[i][it - 1])
                    }

                    board[i][it - 1] = 0
                    break
                }
            }
        }

        return answer
    }
}