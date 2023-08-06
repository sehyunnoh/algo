package main

import "fmt"

func solution(a []int, b []int) bool {
	var diff int
	var first, second int

	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			diff++
			if diff == 1 {
				first = i
			}
			if diff == 2 {
				second = i
			}
			if diff > 2 {
				return false
			}
		}
	}

	if diff == 0 {
		return true
	}

	if diff == 1 {
		return false
	}

	return a[first] == b[second] && a[second] == b[first]
}

func main() {
	a := []int{1, 2, 3}
	b := []int{1, 2, 3}

	fmt.Println(solution(a, b))
}
