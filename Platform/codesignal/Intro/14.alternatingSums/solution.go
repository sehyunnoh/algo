package main

import (
	"fmt"
)

func solution(a []int) []int {
	result := []int{0, 0}
	for i, v := range a {
		result[i%2] += v
	}
	return result
}

func main() {
	a := []int{50, 60, 60, 45, 70}
	fmt.Println(solution(a))
}
