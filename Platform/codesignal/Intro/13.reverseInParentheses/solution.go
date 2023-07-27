package main

import (
	"fmt"
)

func reverse(s string) string {
	result := ""
	for i := len(s) - 1; i >= 0; i-- {
		result += string(s[i])
	}
	return result
}

func solution(s string) string {
	for {
		start := -1
		end := -1
		for i := 0; i < len(s); i++ {
			if s[i] == '(' {
				start = i
			} else if s[i] == ')' {
				end = i
				s = s[:start] + reverse(s[start+1:end]) + s[end+1:]
				break
			}
		}
		if start == -1 {
			return s
		}
	}
}

func main() {
	s := "a(bc(de))"
	fmt.Println(solution(s))
}
