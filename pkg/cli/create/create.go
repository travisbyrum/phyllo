package create

import (
	"fmt"
	"html/template"
	"os"
	"path/filepath"

	"github.com/bobappleyard/readline"
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

func flagReadDefault(c *cli.Context, name string) (string, error) {
	if c.String(name) == "" {
		userPrompt := fmt.Sprintf(">Please provide project %s:", name)

		return readline.String(userPrompt)
	}

	return c.String(name), nil
}

func getFlagInputs(c *cli.Context) (projectData, error) {
	var err error

	t := projectData{}

	if c.NArg() < 1 {
		return t, cli.NewExitError("Please provide project name", 2)
	}

	t.Title = c.Args().Get(0)

	t.Author, err = flagReadDefault(c, "author")
	if err != nil {
		return t, err
	}

	t.Email, err = flagReadDefault(c, "email")
	if err != nil {
		return t, err
	}

	t.Description, err = flagReadDefault(c, "description")
	if err != nil {
		return t, err
	}

	return t, nil
}

//Flags returns the default cli flags for the create subcommand.
func Flags() []cli.Flag {
	return []cli.Flag{
		cli.StringFlag{
			Name:   "author, a",
			Value:  "",
			Usage:  "Project author",
			EnvVar: "PHYLLO_AUTHOR",
		},
		cli.StringFlag{
			Name:   "email, e",
			Value:  "",
			Usage:  "Project email",
			EnvVar: "PHYLLO_EMAIL",
		},
		cli.StringFlag{
			Name:  "description, d",
			Value: "",
			Usage: "Project description",
		},
	}
}

func renderTemplate(path string, tmpl string, data projectData) error {
	templateFile, err := os.Create(path)

	if err != nil {
		return err
	}

	return templates.ExecuteTemplate(templateFile, tmpl, data)
}

//Action defines the default helper for the create subcommand.  This function
//creates the necessary template files and renders them with the provided args.
func Action(c *cli.Context) error {
	t, err := getFlagInputs(c)

	if err != nil {
		return err
	}

	dirs := []string{
		"tests",
		"conf",
		"bin",
		"docs",
		t.Title,
		filepath.Join(t.Title, "resources"),
	}

	templateInfoMap := map[string]string{
		"setup.py":      "setup.py",
		"setup.cfg":     "setup.cfg",
		"tox.ini":       "tox.ini",
		".coveragerc":   ".coveragerc",
		".gitignore":    ".gitignore",
		".pylintrc":     ".pylintrc",
		"Dockerfile":    "Dockefile",
		"MANIFEST.in":   "MANIFEST.in",
		"Pipfile":       "Pipfile",
		"Makefile":      "Makefile",
		"README.md":     "README.md",
		"entrypoint.sh": filepath.Join("bin", "entrypoint.sh"),
		"__init__.py":   filepath.Join(t.Title, "__init__.py"),
		"common.py":     filepath.Join(t.Title, "common.py"),
		"config.py":     filepath.Join(t.Title, "config.py"),
		"extensions.py": filepath.Join(t.Title, "extensions.py"),
		"models.py":     filepath.Join(t.Title, "models.py"),
		"resources.py":  filepath.Join(t.Title, "resources", "__init__.py"),
		"ping.py":       filepath.Join(t.Title, "resources", "ping.py"),
	}

	for _, dir := range dirs {
		err := os.MkdirAll(filepath.Join(t.Title, dir), os.ModePerm)

		if err != nil {
			return err
		}
	}

	for k, v := range templateInfoMap {
		path := filepath.Join(t.Title, v)

		err := renderTemplate(path, k, t)

		if err != nil {
			return err
		}

	}

	return nil
}
