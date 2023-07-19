package main

import (
	"fmt"
	"sort"
)

func solution(a []int) []int {
	p := make([]int, 0)
	for _, v := range a {
		if v != -1 {
			p = append(p, v)
		}
	}

	sort.Ints(p)
	index := 0
	for i, v := range a {
		if v != -1 {
			a[i] = p[index]
			index++
		}
	}

	return a
}

func main() {
	arr := []int{-1, 150, 190, 170, -1, -1, 160, 180}
	fmt.Println(solution(arr))
}
