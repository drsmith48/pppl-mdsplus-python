
include ../../../docs/config/doxygen.am

# //////////////////////////////////////////////////////////////////////////// #
# DOXYGEN CONFIG #

DX_CONFIG = ${top_srcdir}/docs/config/doxygen_cpp.cfg
DX_DOCDIR = mdsobjects/python/docs
DX_PACKAGE_NAME = mdsobjects_py
DX_TITLE = MDSplus Python interface
DX_BRIEF = "MDSplus object oriented interface"

DX_PAGES = .. \
           index.md

DX_EXCLUDE_PAGES = \
                   ../yacc.py \
                   ../lex.py \
                   ../tdiparsetab.py \
                   ../tdilextab.py \
                   ../tdicompile.py \
                   ../mdsExceptions.py \
                   ../setup.py \
                   ../__init__.py
                   
DX_TAGFILES = docs.tag

MOSTLYCLEANFILES = $(DX_CLEANFILES)

# //////////////////////////////////////////////////////////////////////////// #
# TARGETS #

all: html

html: doxygen-run
pdf:  doxygen-pdf

install-data-local: doxygen-install
