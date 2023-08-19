package main

import (
	"fmt"
	"strconv"
	"strings"
)

func solution(s string) bool {
	arr := strings.Split(s, ".")
	if len(arr) != 4 {
		return false
	}
	for i := 0; i < len(arr); i++ {
		if arr[i] == "" {
			return false
		}
		num, err := strconv.Atoi(arr[i])
		if err != nil {
			return false
		}
		if num < 0 || num > 255 {
			return false
		}
		if len(arr[i]) != LenNum(num) {
			return false
		}
	}
	return true
}

func LenNum(s int) int {
	result := 1
	for s >= 10 {
		s = s / 10
		result++
	}
	return result
}

func main() {
	str := "172.16.254.1"
	fmt.Println(solution(str))
}
