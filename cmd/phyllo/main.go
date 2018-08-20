package main

import (
	"log"
	"os"

	"github.com/urfave/cli"

	"phyllo/pkg/cli/commands"
)

const name string = "phyllo"

func main() {
	app := cli.NewApp()
	app.Commands = commands.Commands()
	app.Name = name
	app.Version = commands.Version
	app.Usage = commands.Usage

	err := app.Run(os.Args)

	if err != nil {
		log.Fatal(err)
	}
}
