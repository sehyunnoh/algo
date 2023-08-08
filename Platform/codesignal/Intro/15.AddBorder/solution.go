package main

import "fmt"

func solution(p []string) []string {
	var a string
	for i := 0; i < len(p[0])+2; i++ {
		a += "*"
	}
	var b []string
	b = append(b, a)
	for i := 0; i < len(p); i++ {
		b = append(b, "*"+p[i]+"*")
	}
	b = append(b, a)
	return b
}

func main() {
	fmt.Println(solution([]string{"abc", "ded"}))
}
