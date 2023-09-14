package main

import "fmt"

func solution(n, f int) int {
	return (f + n/2) % n
}

func main() {
	n := 10
	f := 2
	fmt.Println(solution(n, f))
}
