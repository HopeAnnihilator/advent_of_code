package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
)

// i hate go
func b2i(b bool) int {
	if b {
		return 1
	}
	return 0
}

// check repetitions in line
func check_frequency(frequencies map[rune]int, i int) int {
	for key := range frequencies {
		if frequencies[key] == i {
			return 1
		}
	}
	return 0
}

// find matching lines
func check_lines(l1 string, l2 string) bool {
	var total int = 0
	for i := range l1 {
		total += b2i(l1[i] == l2[i])
	}
	return total >= (len(l1) - 1)
}

func main() {
	totals := make(map[int]int)
	var lines []string
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
		// find how many lines contain multiple of a character
		frequencies := make(map[rune]int)
		lines = append(lines, reader.Text())
		// iterate line
		for _, chr := range lines[len(lines)-1] {
			frequencies[chr] += 1
		}
		// add repetitions to totals
		totals[2] += check_frequency(frequencies, 2)
		totals[3] += check_frequency(frequencies, 3)
	}

	// print checksum
	fmt.Println("Checksum:", totals[2]*totals[3])

	// find common characters
	sort.Strings(lines)
	for i := range lines[0 : len(lines)-1] {
		if check_lines(lines[i], lines[i+1]) {
			out := ""
			for c := range lines[i] {
				if lines[i][c] == lines[i+1][c] {
					out += string(lines[i][c])
				}
			}
			println("Common Characters:", out)
			break
		}
	}
}
