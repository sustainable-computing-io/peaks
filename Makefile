SRC_ROOT           := $(shell pwd)

ifndef GOPATH
	GOPATH := $(HOME)/go
endif

ifndef GOBIN
	GOBIN := $(GOPATH)/bin
endif
# for testsuite
ENVTEST_ASSETS_DIR=$(SRC_ROOT)/test-bin
export PATH := $(PATH):$(SRC_ROOT)/test-bin

### toolkit ###
tidy-vendor:
	go mod tidy -v
	go mod vendor

escapes_detect: tidy-vendor
	@go build -gcflags="-m -l" ./... 2>&1 | grep "escapes to heap" || true

set_govulncheck:
	@go install golang.org/x/vuln/cmd/govulncheck@latest

govulncheck: set_govulncheck tidy-vendor
	@govulncheck -v ./... || true

ginkgo-set:
	mkdir -p $(GOBIN)
	mkdir -p $(ENVTEST_ASSETS_DIR)
	@test -f $(ENVTEST_ASSETS_DIR)/ginkgo || \
	 (go install -mod=mod github.com/onsi/ginkgo/v2/ginkgo@v2.4.0  && \
	  cp $(GOBIN)/ginkgo $(ENVTEST_ASSETS_DIR)/ginkgo)

test-verbose: ginkgo-set tidy-vendor
	@go test -covermode=atomic -coverprofile=coverage.out -v $$(go list ./... | grep pkg | grep -v bpfassets) --race --bench=. -cover --count=1 --vet=all
	