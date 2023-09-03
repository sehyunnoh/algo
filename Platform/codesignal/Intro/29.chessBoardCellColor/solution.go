package main

import (
	"fmt"
	"math"
)

func solution(c1, c2 string) bool {
	return int(math.Abs(float64(c2[0]-c1[0]))) % 2 == int(math.Abs(float64(c2[1]-c1[1]))) % 2
}

func main() {
	c1 := "A1"
	c2 := "C3"

	fmt.Println(solution(c1, c2))
}
