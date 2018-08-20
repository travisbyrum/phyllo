package create

import (
	"html/template"
	"os"
	"path/filepath"

	"github.com/urfave/cli"
)

//Usage stores the default help message for the create subcommand.
const Usage string = "Create a new project powered by phyllo"

var templates = template.New("base")

type projectData struct {
	Author      string
	Description string
	Email       string
	Title       string
}

func init() {
	templates = template.Must(template.ParseGlob("assets/*"))
}

//Flags returns the default cli flags for the create subcommand.
func Flags() []cli.Flag {
	return []cli.Flag{
		cli.StringFlag{
			Name:  "title",
			Value: "",
			Usage: "Project title",
		},
	}
}

func renderTemplate(projectPath string, tmpl string, data projectData) error {
	templateFile, err := os.Create(filepath.Join(projectPath, tmpl))

	if err != nil {
		return err
	}

	return templates.ExecuteTemplate(templateFile, tmpl, data)
}

//Action defines the default helper for the create subcommand.  This function
//creates the necessary template files and renders them with the provided args.
func Action(c *cli.Context) error {
	t := projectData{}

	if c.NArg() < 1 {
		return cli.NewExitError("Please provide project name", 2)
	}

	t.Title = c.Args().Get(0)

	err := os.MkdirAll(filepath.Join(t.Title, t.Title), os.ModePerm)

	if err != nil {
		return err
	}

	err = renderTemplate(t.Title, "setup.py", t)

	if err != nil {
		return err
	}

	return nil
}
