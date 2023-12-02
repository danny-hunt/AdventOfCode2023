package main

import (
	_ "embed"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

// var {
// 	//go:generate cp -r ../../inputs ./local-asset-dir
// 	//go:embed local-asset-dir/02.in
// 	Input string
// }

type CubeSet struct {
	Red   int
	Green int
	Blue  int
}

type Game struct {
	ID   int
	Sets []CubeSet
}

func parse(input string) Game {
	sets := make([]CubeSet, 0)
	parts := strings.Split(input, ":")
	gameString, trialSets := parts[0], parts[1]

	// log.Printf("Parsing game %s", gameString)

	gameIdParts := strings.Split(gameString, " ")
	_, gameIdStr := gameIdParts[0], gameIdParts[1]
	gameID, _ := strconv.Atoi(gameIdStr)

	trialSetsList := strings.Split(trialSets, ";")
	for _, trialSet := range trialSetsList {
		colors := strings.Split(trialSet, ",")
		red, green, blue := 0, 0, 0
		for _, colorString := range colors {
			countColor := strings.Split(strings.TrimSpace(colorString), " ")
			count, color := countColor[0], countColor[1]

			countInt, _ := strconv.Atoi(count)
			switch color {
			case "red":
				red = countInt
			case "green":
				green = countInt
			case "blue":
				blue = countInt
			default:
				panic(fmt.Sprintf("Unknown color: %s", color))
			}
		}
		cubeSet := CubeSet{Red: red, Green: green, Blue: blue}
		sets = append(sets, cubeSet)
	}

	return Game{ID: gameID, Sets: sets}
}

func isValidCubeSet(cubeSet CubeSet) bool {
	const maxRed, maxGreen, maxBlue = 12, 13, 14
	return cubeSet.Red <= maxRed && cubeSet.Green <= maxGreen && cubeSet.Blue <= maxBlue
}

func partOne(input string) int {
	games := parseInput(input, parse)
	successfulIDTotal := 0

	for _, game := range games {
		if isValidGame(game) {
			successfulIDTotal += game.ID
		}
	}

	return successfulIDTotal
}

func partTwo(input string) int {
	games := parseInput(input, parse)
	total := 0

	for _, game := range games {
		minRed := maxCubeSetValue(game.Sets, func(cs CubeSet) int { return cs.Red })
		minGreen := maxCubeSetValue(game.Sets, func(cs CubeSet) int { return cs.Green })
		minBlue := maxCubeSetValue(game.Sets, func(cs CubeSet) int { return cs.Blue })

		cubePower := minRed * minGreen * minBlue
		total += cubePower
	}

	return total
}

func parseInput(input string, parser func(string) Game) []Game {
	lines := strings.Split(input, "\n")

	games := make([]Game, 0)
	for _, line := range lines {
		if line != "" {
			game := parser(line)
			games = append(games, game)
		}
	}

	return games
}

func maxCubeSetValue(sets []CubeSet, getValue func(CubeSet) int) int {
	maxValue := 0
	for _, set := range sets {
		value := getValue(set)
		if value > maxValue {
			maxValue = value
		}
	}
	return maxValue
}

func isValidGame(game Game) bool {
	// log.Printf("Checking game %d", game)
	return all(func(cubeSet CubeSet) bool { return isValidCubeSet(cubeSet) }, game.Sets)
}

func all(predicate func(CubeSet) bool, sets []CubeSet) bool {
	for _, set := range sets {
		if !predicate(set) {
			return false
		}
	}
	return true
}

func timer(fn func() int) int {
	start := time.Now()
	result := fn()
	elapsed := time.Since(start).Milliseconds()

	fmt.Printf("Execution time: %dms\n", elapsed)

	return result
}

func main() {
	input, _ := os.ReadFile("../../inputs/02.in")
	answer1 := timer(func() int {
		return partOne(string(input))
	})
	answer2 := timer(func() int {
		return partTwo(string(input))
	})

	log.Printf("Solution: %d, %d", answer1, answer2)
}
