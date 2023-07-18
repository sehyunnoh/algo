package main

import (
	"fmt"
	"strconv"
)

func solution(n int) bool {

	str := strconv.Itoa(n)
	half := len(str) / 2
	firstCnt := 0
	for _, x := range str[:half] {
		number, _ := strconv.Atoi(string(x))
		firstCnt += number
	}

	secondCnt := 0
	for _, x := range str[half:] {
		number, _ := strconv.Atoi(string(x))
		secondCnt += number
	}

	return firstCnt == secondCnt
}

func main() {

	n := 1230
	fmt.Println(solution(n))
}
