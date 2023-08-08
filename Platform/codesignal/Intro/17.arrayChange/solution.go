package main

import "fmt"

func solution(arr []int) int {
	var result = 0
	var diff = 0
	for i := 1; i < len(arr); i++ {
		if arr[i] <= arr[i-1] {
			diff = arr[i-1] - arr[i] + 1
			result += diff
			arr[i] += diff
		}
	}
	return result
}

func main() {
	arr := []int{-1000, 0, -2, 0}
	fmt.Println(solution(arr))
}
