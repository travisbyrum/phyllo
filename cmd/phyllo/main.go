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
	app.Name = name
	app.Usage = commands.Usage
	app.Version = commands.Version

	app.Commands = commands.Commands()

	err := app.Run(os.Args)

	if err != nil {
		log.Fatal(err)
	}
}
