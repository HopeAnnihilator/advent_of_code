package main

import (
	"bufio"
	"log"
	"os"
	"sort"
)

// process polymer by removing consecutive chars with varying case
func react_polymer(polymer []byte) []byte {
	for {
		change := false
		for i := 0; i < len(polymer)-2; i++ {
			if ((polymer[i] + 0x20) == polymer[i+1]) || ((polymer[i] - 0x20) == polymer[i+1]) {
				polymer = append(polymer[:i], polymer[i+2:]...)
				change = true
				i--
			}
		}
		if !change {
			break
		}
	}
	return polymer
}

// strip upper and lowercase char from polymer
func strip_polymer(polymer []byte, chr int) []byte {
	for {
		change := false
		for i := 0; i < len(polymer)-1; i++ {
			if (uint8(polymer[i]) == uint8(0x41+chr)) || (uint8(polymer[i]) == uint8(0x61+chr)) {
				polymer = append(polymer[:i], polymer[i+1:]...)
				change = true
				i--
			}
		}
		if !change {
			break
		}
	}
	return polymer
}

func main() {
	// get sys args
	args := os.Args
	if len(args) < 1 {
		log.Fatal("Run as: ./day05 ./input.txt")
	}

	// open input file
	file, err := os.Open(args[1])
	if err != nil {
		log.Fatal(err)
	}

	// read a line from input
	reader := bufio.NewScanner(file)
	reader.Scan()
	inData := reader.Bytes()

	// copy input to new byte array and process polymer
	polymer := make([]byte, len(inData))
	copy(polymer, inData)
	polymer = react_polymer(polymer)

	println("Units remaining after reacting polymer:", len(polymer))

	// remove aA-zZ from input and process polymer
	polyLens := [26]int{}
	for i := 0; i < 26; i++ {
		tmpPoly := make([]byte, len(inData))
		copy(tmpPoly, inData)
		tmpPoly = strip_polymer(tmpPoly, i)
		tmpPoly = react_polymer(tmpPoly)
		polyLens[i] = len(tmpPoly)
	}

	// create slice from backing array and sort
	polyLensSlice := polyLens[:]
	sort.Ints(polyLensSlice)

	println("Shortest polymer:", polyLensSlice[0])
}
