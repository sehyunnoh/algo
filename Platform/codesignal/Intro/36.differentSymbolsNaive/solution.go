package main

import "fmt"

func solution(s string) int {
	m := make(map[rune]bool)
	for _, v := range s {
		m[v] = true
	}
	return len(m)
}

func main() {
	s := "cabca"
	fmt.Println(solution(s))
}
