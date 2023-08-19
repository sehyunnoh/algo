package main

import (
	"fmt"
	"sort"
)

func solution(arr []int) int {
	sort.Ints(arr)
	n := 2
	for n < arr[len(arr)-1] {
		isDivided := false
		for _, x := range arr {
			if x%n == 0 {
				isDivided = true
				break
			}
		}
		if !isDivided {
			return n
		}
		n++
	}
	return arr[len(arr)-1] + 1
}

func main() {
	arr := []int{5, 3, 6, 7, 9}
	fmt.Println(solution(arr))
}
