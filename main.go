package main

import (
	"fmt"
	"io/ioutil"
	"log"

	hclParser "github.com/hashicorp/hcl/hcl/parser"
)


func main() {
	log.Println("--- Parsing HCL ---")

	d, err := ioutil.ReadFile("./s3.tf")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(d))

	if astFile, err := hclParser.Parse([]byte(string(d))); err == nil {
		fmt.Println(astFile)
	} else {
		fmt.Println("Parsing failed.")
	}
	fmt.Println(astFile.name)

	log.Println("--- Generate HCL ---")
}
