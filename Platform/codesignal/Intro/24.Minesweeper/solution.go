package main

import "fmt"

func solution(m [][]bool) [][]int {

	row := len(m)
	col := len(m[0])

	var result [][]int
	for i := 0; i < row; i++ {
		var row []int
		for j := 0; j < col; j++ {
			row = append(row, 0)
		}
		result = append(result, row)
	}

	for r := 0; r < row; r++ {
		for c := 0; c < col; c++ {
			n := 0
			if (r-1) >= 0 && (c-1) >= 0 && m[r-1][c-1] {
				n++
			}
			if (r-1) >= 0 && m[r-1][c] {
				n++
			}
			if (r-1) >= 0 && (c+1) < col && m[r-1][c+1] {
				n++
			}
			if (c+1) < col && m[r][c+1] {
				n++
			}
			if (r+1) < row && (c+1) < col && m[r+1][c+1] {
				n++
			}
			if (r+1) < row && m[r+1][c] {
				n++
			}
			if (r+1) < row && (c-1) >= 0 && m[r+1][c-1] {
				n++
			}
			if (c-1) >= 0 && m[r][c-1] {
				n++
			}
			result[r][c] = n
		}
	}
	return result
}

func main() {

	m := [][]bool{
		{true, false, false},
		{false, true, false},
		{false, false, false},
	}

	fmt.Println(solution(m))

}
