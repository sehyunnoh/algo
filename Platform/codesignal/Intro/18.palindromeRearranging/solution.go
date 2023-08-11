package main

import "fmt"

func solution(s string) bool {
	acc := make(map[string]int)
	for _, x := range s {
		str := string(x)
		_, exists := acc[str]

		if exists {
			acc[str] += 1
		} else {
			acc[str] = 1
		}
	}

	odd_num := 0
	for _, v := range acc {
		if v%2 == 1 {
			odd_num++
		}
	}
	return odd_num <= 1
}

func main() {
	s := "aabb"
	fmt.Print(solution(s))
}
