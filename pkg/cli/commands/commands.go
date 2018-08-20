/*
phyllo is a command line utility to quickly create python apis from tepmlate.

NAME:
   phyllo - Python api creator

USAGE:
   phyllo [global options] command [command options] [arguments...]

VERSION:
   0.0.1

COMMANDS:
     create   Create a new project powered by phyllo
     help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --help, -h     show help
   --version, -v  print the version
*/

package commands

import (
	"github.com/urfave/cli"

	"phyllo/pkg/cli/create"
)

//Version stores the default package version.
const Version string = "0.0.1"

//Usage stores the default help message for the create subcommand.
const Usage string = "Python api creator"

//Commands returns an array of cli commands to add to main.
func Commands() []cli.Command {
	return []cli.Command{
		{
			Name:   "create",
			Usage:  create.Usage,
			Flags:  create.Flags(),
			Action: create.Action,
		},
	}
}
