package main

import "fmt"

func solution(d, r, t int) int {
	year := 0
	fd := float64(d)
	for fd < float64(t) {
		fd = fd + fd*float64(r)/100
		year++
	}
	return year
}

func main() {
	// fmt.Println(solution(100, 20, 170))
	// fmt.Println(solution(70, 10, 77))
	fmt.Println(solution(1, 1, 200))
}
