MAKEFLAGS += --silent
PACKAGE := phyllo
GOVERSION := $(shell go version | awk '{print $$3;}')
BIN := $(GOPATH)/bin
BASE := $(GOPATH)/bin
GO_CMD := $(shell which go)
GO_BUILD := $(GO_CMD) build
GO_RUN := $(GO_CMD) run
GO_TEST := $(GO_CMD) test
GO_INSTALL := $(GO_CMD) install -v
GO_FMT := $(GO_CMD) fmt
GO_DOC := $(shell which godoc)
MAIN := cmd/$(PACKAGE)/main.go

all: build

.PHONY: all

build:
	mkdir -p ./bin
	rm -f ./bin/*
	$(GO_BUILD) -o ./bin/$(PACKAGE) $(MAIN)

.PHONY: build

dist:
	mkdir -p ./bin
	rm -f ./bin/*
	GOOS=darwin GOARCH=amd64 $(GO_BUILD) -o ./bin/$(PACKAGE)-darwin64 ./...
	GOOS=linux GOARCH=amd64 $(GO_BUILD) -o ./bin/$(PACKAGE)-linux64 ./...
	GOOS=linux GOARCH=386 $(GO_BUILD) -o ./bin/$(PACKAGE)-linux386 ./...

.PHONY: dist

install:
	$(GO_INSTALL) ./...

.PHONY: install

test:
	$(GO_TEST) -v ./...

.PHONY: test

doc:
	$(GO_DOC) -http=":6060"

.PHONY: doc

run:
	$(GO_RUN) $(MAIN)

.PHONY: run

lint:
	$(GO_FMT) ./...

.PHONY: lint