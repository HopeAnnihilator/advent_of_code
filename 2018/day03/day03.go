package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	const CANVAS_SIZE = 1000
	arr := [CANVAS_SIZE][CANVAS_SIZE]int{}
	var lines []string

	// get sys args
	args := os.Args
	if len(args) < 1 {
		log.Fatal("Run as: ./day03 ./input.txt")
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
		lines = append(lines, reader.Text())
		inData := strings.Split(reader.Text(), " ")
		location := strings.Split(strings.Replace(inData[2], ":", "", 1), ",")
		size := strings.Split(inData[3], "x")
		xLoc, _ := strconv.Atoi(location[0])
		yLoc, _ := strconv.Atoi(location[1])
		xRange, _ := strconv.Atoi(size[0])
		yRange, _ := strconv.Atoi(size[1])
		for x := 0; x < xRange; x++ {
			for y := 0; y < yRange; y++ {
				arr[xLoc+x][yLoc+y] += 1
			}
		}
	}
	total := 0
	for x := 0; x < CANVAS_SIZE; x++ {
		for y := 0; y < CANVAS_SIZE; y++ {
			if arr[x][y] >= 2 {
				total++
			}
		}
	}
	println("Total Overlaps:", total)
	for i := range lines[0 : len(lines)-1] {
		inData := strings.Split(lines[i], " ")
		location := strings.Split(strings.Replace(inData[2], ":", "", 1), ",")
		size := strings.Split(inData[3], "x")
		xLoc, _ := strconv.Atoi(location[0])
		yLoc, _ := strconv.Atoi(location[1])
		xRange, _ := strconv.Atoi(size[0])
		yRange, _ := strconv.Atoi(size[1])
		flag := true
		for x := 0; x < xRange; x++ {
			for y := 0; y < yRange; y++ {
				if arr[xLoc+x][yLoc+y] > 1 {
					flag = false
				}
			}
		}
		if flag {
			println(strings.Replace(inData[0], "#", "", 1), "does not overlap")
		}
	}
}
