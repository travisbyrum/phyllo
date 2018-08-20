# {{.Title}}

{{.Description}}

## Installation

To install the minimum version of this project run the following from the root directory:

```bash
make install
```

To install the development version of the api run:

```bash
make install-dev
```

To run the development server you can use the cli that comes with the package. This cli inherits all methods available through [Flask](http://flask.pocoo.org/docs/0.12/cli/). To install via [Docker](https://www.docker.com) run:

```bash
make docker-build && make docker-rin
```

## Testing

Testing in this package uses [pytest](https://docs.pytest.org) as the default test runner. The tests in this packages are available in the `tests` directory being split between `unit` and `integration` tests.

All tests can run through the following command:

```bash
make test
```

Coverage reports can be generated through:

```bash
make coverage
```

### Style

Linting is accomplished through [pylint](https://www.pylint.org) with the following [configuration](.pylintrc). Package source code can be linted by running:

```bash
make lint
```

## Built With

- [flask](http://flask.pocoo.org) - Web framework
- [SQLAlchemy](http://www.sqlalchemy.org) - Package ORM
- [pylint](https://www.pylint.org) - Linting
- [pytest](https://docs.pytest.org) - Test management
- [coverage](https://coverage.readthedocs.io/en/coverage-4.5.1a/) - Code coverage

## Authors

- **{{.Author}}** - _Initial work_

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
