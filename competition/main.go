package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// readLine reads a line from standard input, splits it by the given separator,
// and returns a slice of the specified type T.
func readLine[T string | int](sep string) []T {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	inputs := strings.Split(scanner.Text(), sep)
	var result []T
	for _, v := range inputs {
		var val T
		switch any(val).(type) {
		case string:
			result = append(result, any(v).(T))
		case int:
			i, err := strconv.Atoi(v)
			if err != nil {
				panic("failed to convert string to int: " + v)
			}
			result = append(result, any(i).(T))
		default:
			panic("unsupported type")
		}
	}

	return result
}

func main() {
	inputs := readLine[int](" ")
	A, B, C := inputs[0], inputs[1], inputs[2]
	fmt.Printf("%d %d %d\n", A, B, C)
}
