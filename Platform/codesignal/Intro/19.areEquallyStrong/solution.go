package main

import (
	"fmt"
	"math"
)

func solution(yl int, yr int, fl int, fr int) bool {
	return math.Max(float64(yl), float64(yr)) == math.Max(float64(fl), float64(fr)) && (yl+yr) == (fl+fr)
}

func main() {
	yl, yr, fl, fr := 10, 15, 15, 10
	fmt.Print(solution(yl, yr, fl, fr))
}
