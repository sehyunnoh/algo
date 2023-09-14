package main

import "fmt"

func solution(s string) string {
	res := ""
	for _, c := range s {
		if c == 'z' {
			res += "a"
		} else {
			res += string(c + 1)
		}
	}
	return res
}

func main() {
	s := "crazy"
	fmt.Println(s)
}
