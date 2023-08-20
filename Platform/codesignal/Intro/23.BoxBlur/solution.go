package main

import "fmt"

func solution(image [][]int) [][]int {
	row := len(image) - 2
	col := len(image[0]) - 2

	var result [][]int
	for i := 0; i < row; i++ {
		var row []int
		for j := 0; j < col; j++ {
			row = append(row, 0)
		}
		result = append(result, row)
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			result[i][j] = (image[i][j] + image[i][j+1] + image[i][j+2] +
				image[i+1][j] + image[i+1][j+1] + image[i+1][j+2] +
				image[i+2][j] + image[i+2][j+1] + image[i+2][j+2]) / 9
		}
	}
	return result
}

func main() {
	image := [][]int{
		{1, 1, 1},
		{1, 7, 1},
		{1, 1, 1},
	}
	fmt.Println(solution(image))
}
