package main

import "fmt"

func solution(n int) bool {
	for n > 0 {
		if n%2 != 0 {
			return false
		}
		n /= 10
	}
	return true
}

func main() {
	n := 248622
	fmt.Println(solution(n))
}
