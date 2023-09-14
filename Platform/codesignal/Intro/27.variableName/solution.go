package main

import "fmt"

func solution(name string) bool {
	if name[0] >= '0' && name[0] <= '9' {
		return false
	}
	for _, x := range name {
		if !((x >= '0' && x <= '9') || (x >= 'a' && x <= 'z') || (x >= 'A' && x <= 'Z') || x == '_') {
			return false
		}
	}
	return true
}

func main() {
	name := "var_1__Int"
	fmt.Println(solution(name))
}
