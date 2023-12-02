package main

import (
	_ "embed"
	"log"
	"os"
	"strings"
	"unicode"
)

// var {
// 	//go:generate cp -r ../../inputs ./local-asset-dir
// 	//go:embed local-asset-dir/01.in
// 	Input string
// }

var NumberWords = []string{
	"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
}

func Map[T, V any](ts []T, fn func(T) V) []V {
	result := make([]V, len(ts))
	for i, t := range ts {
		result[i] = fn(t)
	}
	return result
}

var ReverseNumberWords = Map(NumberWords, reverse)

func firstDigit(input string) (int, int) {
	// Find the first digit in the input.
	// Valid digits are single digits or the word for a single digit
	for i, char := range input {
		if unicode.IsDigit(char) {
			return int(char - '0'), i
		}
	}
	panic("Found no digit")
}

func numberStringToInt(input string) int {
	// convert a word to a number
	// eg "one" -> 1
	for i, word := range NumberWords {
		if input == word {
			return i
		}
	}
	for i, word := range ReverseNumberWords {
		if input == word {
			return i
		}
	}
	panic("Found no digit")
}

func findEarliestSubstring(substrings []string, target string) (int, int) {
	earliestIndex := len(target) // Initialize with a value greater than any possible index
	earliestSubstring := ""

	for _, substring := range substrings {
		index := strings.Index(target, substring)
		if index != -1 && index < earliestIndex {
			earliestIndex = index
			earliestSubstring = substring
		}
	}

	if earliestSubstring != "" {
		return numberStringToInt(earliestSubstring), earliestIndex
	}
	return 0, -1
}

func FirstNumber(input string) int {
	// Find the first "number" in the input string.
	// Valid numbers are single digits or the word for a single digit
	// eg 2, 5, one, four, 7 are all valid numbers

	for _, char := range input {
		if unicode.IsDigit(char) {
			return int(char - '0')
		}

	}
	log.Printf("Found no digit")
	return 0
}

// Returns two integers, the first one is the solution for part 1, the second one for part 2
func Solve(input string) (int, int) {
	total := 0
	for _, line := range strings.Split(input, "\n") {
		first_digit, _ := firstDigit(line)
		last_digit, _ := firstDigit(reverse(line))
		additional_bit := first_digit*10 + last_digit
		// total += first_digit*10 + last_digit
		total += additional_bit
	}

	secondTotal := 0
	for _, line := range strings.Split(input, "\n") {
		firstNum, firstNumIndex := firstDigit(line)
		firstWord, firstWordIndex := findEarliestSubstring(NumberWords, line)
		lastWord, lastWordIndex := findEarliestSubstring(ReverseNumberWords, reverse(line))
		lastNum, lastNumIndex := firstDigit(reverse(line))
		var first, last int
		if 0 < firstWordIndex && firstWordIndex < firstNumIndex {
			first = firstWord
		} else {
			first = firstNum
		}
		if 0 < lastWordIndex && lastWordIndex < lastNumIndex {
			last = lastWord
		} else {
			last = lastNum
		}
		// log.Printf("Found %d + %d = %s", first, last, line)
		secondTotal += first*10 + last
	}
	// log.Println(ReverseNumberWords)
	return total, secondTotal

}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	input, _ := os.ReadFile("../../inputs/01.in")
	answer1, answer2 := Solve(string(input))
	log.Printf("Solution: %d, %d", answer1, answer2)
}
