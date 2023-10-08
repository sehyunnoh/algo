package main

import "fmt"

func solution(s string) string {
	for _, v := range s {
		if v >= '0' && v <= '9' {
			return string(v)
		}
	}
	return ""
}

func main() {
	s := "var_1__Int"
	fmt.Println(solution(s))
}
