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
