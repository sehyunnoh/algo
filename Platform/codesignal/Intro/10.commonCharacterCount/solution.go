package main

import "fmt"

func solution(s1 string, s2 string) int {
	result := 0
	set := make(map[rune]bool)
	for _, x := range s1 {
		set[x] = true
	}

	for k, _ := range set {
		// s1
		s1Cnt := 0
		for _, x := range s1 {
			if x == k {
				s1Cnt++
			}
		}
		// s2
		s2Cnt := 0
		for _, x := range s2 {
			if x == k {
				s2Cnt++
			}
		}

		if s1Cnt < s2Cnt {
			result += s1Cnt
		} else {
			result += s2Cnt
		}
	}

	return result
}

func main() {
	s1 := "aabcc"
	s2 := "adcaa"

	fmt.Println(solution(s1, s2))
}
