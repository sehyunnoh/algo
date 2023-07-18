package main

import "fmt"

func solution(arr []string) []string {
	max := 0
	for _, x := range arr {
		if len(x) > max {
			max = len(x)
		}
	}

	result := make([]string, 0, 5)
	for _, x := range arr {
		if len(x) == max {
			result = append(result, x)
		}
	}

	return result
}

func main() {
	arr := []string{"aba", "aa", "ad", "vcd", "aba"}
	fmt.Println(solution(arr))
}
