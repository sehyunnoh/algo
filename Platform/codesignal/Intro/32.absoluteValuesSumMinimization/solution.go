package main

import (
	"fmt"
	"math"
)

func solution(a []int) int {
	min, index := math.MaxInt64, 0
	for i := 0; i < len(a); i++ {
		sum := 0
		for j := 0; j < len(a); j++ {
			if i == j {
				continue
			}
			sum += int(math.Abs(float64(a[j] - a[i])))
		}
		if sum < min {
			min = sum
			index = i
		}
	}
	return a[index]
}

func main() {
	a := []int{2, 4, 7}
	fmt.Println(solution(a))
}
