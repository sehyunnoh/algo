package main

import (
	"fmt"
)

func solution(arr []int) int {
	result, diff := 0, 0
	for i := 1; i < len(arr); i++ {
		diff = (arr[i] - arr[i-1])
		if diff < 0 {
			diff *= -1
		}
		if diff > result {
			result = diff
		}
	}
	return result
}

func main() {
	arr := []int{2, 4, 1, 0}
	fmt.Print(solution(arr))
}
