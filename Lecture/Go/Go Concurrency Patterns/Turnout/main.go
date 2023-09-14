package main

func Turnout (IntA, Inb <- chan int, OutA, OutB chan int) { 
	for {
		select {
		case data, more := <- IntA:
		case data, more := <- Inb:
		}

		select {
		case OutA <- data:
		case OutB <- data:
		}
}