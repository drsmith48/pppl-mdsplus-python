ANACONDA2 = /usr/pppl/anaconda2/4.4.0/bin
ANACONDA3 = /usr/pppl/anaconda3/4.4.0/bin

define PRINT_HELP_PYSCRIPT
import re, sys
print("Makefile targets:")
for line in sys.stdin:
	match = re.match(r'^([0-9a-zA-Z_. -]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		for word in target.split():
			print("%-20s %s" % (word, help))
endef
export PRINT_HELP_PYSCRIPT

.PHONY: help
help: ## show this help message
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: mdsplus
mdsplus: ## Build and test Python package for MDSplus release
	$(eval mdsdir := pylib/$@)
	@echo "****************************************************"
	@echo "*** Start: $(mdsdir)"
	@echo "MDSplus installation: $(MDSPLUS)"
	@echo "Building and testing with python2"
	@$(MAKE) build mdsdir=$(mdsdir) pybase=$(ANACONDA2)
	@$(MAKE) test mdsdir=$(mdsdir) pybase=$(ANACONDA2)
	@echo "*** Successful build and test: $(mdsdir)"
	@echo "****************************************************"
	
.PHONY: mdsplus_alpha v6.1.84 v7.0.71 v7.1.13
mdsplus_alpha v6.1.84 v7.0.71 v7.1.13: ## Build and test Python package for MDSplus release
	$(eval mdsdir := pylib/$@)
	@echo "****************************************************"
	@echo "*** Start: $(mdsdir)"
	@echo "MDSplus installation: $(MDSPLUS)"
	@echo "Building with python3 and testing with python2/python3"
	@$(MAKE) build mdsdir=$(mdsdir) pybase=$(ANACONDA3) wheel_flags=--universal
	@$(MAKE) test mdsdir=$(mdsdir) pybase=$(ANACONDA3)
	@$(MAKE) test mdsdir=$(mdsdir) pybase=$(ANACONDA2)
	@echo "*** Successful build and test: $(mdsdir)"
	@echo "****************************************************"

.PHONY: build
build:
	@echo "*** Build & install $(mdsdir) with $(pybase)"
	$(eval python = $(pybase)/python)
	@echo "Using python: $(python)"
	$(eval pip = $(pybase)/pip)
	@echo "Using pip: $(pip)"
	@rm -rf $(mdsdir)/dist $(mdsdir)/build $(mdsdir)/package
	@echo "Building:"
	cd $(mdsdir) && $(python) setup.py --quiet bdist_wheel $(wheel_flags)
	@echo "Installing:"
	@mkdir -p $(mdsdir)/package
	cd $(mdsdir) && $(pip) install --quiet --no-index --ignore-installed \
	--find-links=dist --target=package MDSplus
	@echo "*** End build & install"

.PHONY: test
test:
	@echo "*** Testing $(mdsdir) with $(pybase)"
	$(eval python = $(pybase)/python)
	@echo "Using python: $(python)"
	$(eval PYTHONPATH := $(mdsdir)/package)
	@echo "PYTHONPATH: $(PYTHONPATH)"
	$(eval PYTHONUSERBASE := '')
	@echo "PYTHONUSERBASE: $(PYTHONUSERBASE)"
	@$(python) --version
	$(python) -c "import MDSplus; print(MDSplus.__file__)"
	$(python) test-mdsplus.py
	@echo "*** End testing"
	
