package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func b2i(b bool) int {
	if b {
		return 1
	}
	return 0
}

func main() {
	var totalp1 int = 0
	var totalp2 int = 0
	// get sys args
	args := os.Args
	if len(args) < 1 {
		log.Fatal("Run as: ./day02 ./input.txt")
	}

	// open input file
	file, err := os.Open(args[1])
	if err != nil {
		log.Fatal(err)
	}

	// create reader and parse by line
	reader := bufio.NewScanner(file)
	reader.Split(bufio.ScanLines)
	for reader.Scan() {
		strategy := strings.Split(reader.Text(), " ")
		opponentMove := int(strategy[0][0]) - 64
		myMove := int(strategy[1][0]) - 88

		// not typecasting bool to int is so much simpler right????????
		totalp1 += 6*b2i(myMove == opponentMove%3) + 3*b2i((opponentMove-1) == myMove) + myMove + 1
		totalp2 += 3*myMove + b2i(myMove == 2)*(opponentMove%3+1) + b2i(myMove == 1)*opponentMove + b2i(myMove == 0)*(opponentMove-1+3*b2i(opponentMove-1 == 0))
	}

	// print total
	fmt.Println("Total Points Part 1:", totalp1)
	fmt.Println("Total Points Part 2:", totalp2)
}
