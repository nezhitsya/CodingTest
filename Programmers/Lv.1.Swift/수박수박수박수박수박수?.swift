func solution(_ n:Int) -> String {
    let extra = String((n % 2 == 0) ? "" : "수")
    return String(repeating: "수박", count: n / 2) + extra
}
