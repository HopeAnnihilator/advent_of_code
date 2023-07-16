package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	var total int = 0
	frequencies := make(map[int]int)
	history := []int{}
	var found bool = false

	// get sys args
	args := os.Args
	if len(args) < 1 {
		log.Fatal("Run as: ./day01 ./input.txt")
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
		// convert line to int
		val, err := strconv.Atoi(reader.Text())
		if err != nil {
			log.Fatal(err)
		}

		// add to total and check frequenices
		total += val
		frequencies[total] += 1
		if (frequencies[total] > 1) && !found {
			fmt.Println("Repeated First:", total)
			found = true
		}
		// save input if frequencies not repeated
		history = append(history, val)
	}

	// print total
	fmt.Println("Total:", total)

	// if no repeating frequencies repeat input until found
	for !found {
		for i := 0; i < len(history); i++ {
			total += history[i]
			frequencies[total] += 1
			if frequencies[total] > 1 {
				fmt.Println("Repeated First:", total)
				found = true
				break
			}
		}
	}
}
