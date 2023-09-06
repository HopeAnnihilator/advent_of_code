package main

import (
	"bufio"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var schedules = map[int]int{}
	var sleepTracker = map[int]map[int]int{}

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

	// parse input into sortable timestamps
	for reader.Scan() {
		inData := strings.Split(reader.Text(), " ")
		date := strings.Split(inData[0][1:], "-")
		month, _ := strconv.Atoi(date[1])
		day, _ := strconv.Atoi(date[2])
		time := strings.Split(strings.Replace(inData[1], "]", "", 1), ":")
		hour, _ := strconv.Atoi(time[0])
		min, _ := strconv.Atoi(time[1])
		timestamp := ((month-1)*31+day)*60*24 + (hour * 60) + min

		switch inData[2][0] {
		case 'G':
			{
				gid, _ := strconv.Atoi(inData[3][1:])
				schedules[timestamp] = gid
			}
		case 'w':
			{
				schedules[timestamp] = 0
			}
		case 'f':
			{
				schedules[timestamp] = -1
			}
		}
	}

	// sort timestamps
	keys := make([]int, 0, len(schedules))
	for k := range schedules {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	currGuard := map[string]int{
		"id":         0,
		"sleepStart": 0,
	}

	// find how long each guard slept and what mins they were asleep
	for _, key := range keys {
		switch schedules[key] {
		case -1:
			{
				currGuard["sleepStart"] = key
			}
		case 0:
			{
				sleepTracker[currGuard["id"]][-1] += key%1440 - currGuard["sleepStart"]%1440
				for i := currGuard["sleepStart"]; i < key; i++ {
					sleepTracker[currGuard["id"]][i%60] += 1
				}
			}
		default:
			{
				currGuard["id"] = schedules[key]
				_, exists := sleepTracker[currGuard["id"]]
				if !exists {
					sleepTracker[currGuard["id"]] = map[int]int{}
				}
			}
		}
	}

	// find which guard slept the most overall and which guard slept most on any given minute
	guardTracker := map[string]int{
		"id":                0,
		"timeSlept":         0,
		"mostSleptMin":      0,
		"mostSleptMinCount": 0,

		"mostSleptAtMin":      0,
		"mostSleptAtMinId":    0,
		"mostSleptAtMinCount": 0,
	}
	for k, v := range sleepTracker {
		if v[-1] > guardTracker["timeSlept"] {
			guardTracker["id"] = k
			guardTracker["timeSlept"] = v[-1]
		}
	}

	for k, v := range sleepTracker[guardTracker["id"]] {
		if (v > guardTracker["mostSleptMinCount"]) && (k >= 0) {
			guardTracker["mostSleptMin"] = k
			guardTracker["mostSleptMinCount"] = v
		}
	}

	for k1, v1 := range sleepTracker {
		for k2, v2 := range v1 {
			if v2 > guardTracker["mostSleptAtMinCount"] && (k2 >= 0) {
				guardTracker["mostSleptAtMin"] = k2
				guardTracker["mostSleptAtMinId"] = k1
				guardTracker["mostSleptAtMinCount"] = v2
			}
		}
	}

	println("Most Slept Guard        :", guardTracker["id"])
	println("Time Slept              :", guardTracker["timeSlept"])
	println("Most Slept Minute       :", guardTracker["mostSleptMin"])
	println("Minute Overlaps         :", guardTracker["mostSleptMinCount"])
	println()
	println("Most Slept At Min Guard :", guardTracker["mostSleptAtMinId"])
	println("Most Slept At Min       :", guardTracker["mostSleptAtMin"])
	println("Most Slept At Min Count :", guardTracker["mostSleptAtMinCount"])
	println()
	println("Part 1 Solution         :", guardTracker["id"]*guardTracker["mostSleptMin"])
	println("Part 2 Solution         :", guardTracker["mostSleptAtMinId"]*guardTracker["mostSleptAtMin"])
}
