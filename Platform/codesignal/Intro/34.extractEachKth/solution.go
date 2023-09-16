package main

import "fmt"

func solution(arr []int, k int) []int {
	result := []int{}
	for i, x := range arr {
		if (i+1)%k != 0 {
			result = append(result, x)
		}
	}
	return result
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	k := 3
	fmt.Println(solution(arr, k))
}
