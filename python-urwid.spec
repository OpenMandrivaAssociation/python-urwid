%define module	urwid

Summary:	Full-featured Python console user interface library

Name: 		python-%{module}
Version:	4.0.8
Release:	1
Source0:	https://pypi.org/packages/source/u/urwid/%{module}-%{version}.tar.gz
License:	LGPL
Group: 		Development/Python
Url: 		https://urwid.org

BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(toml)
BuildRequires:	pkgconfig(python3)

BuildArch:	noarch

%description
Urwid is a console user interface library. It includes many features
useful for text console application developers including :

* Applcations resize quickly and smoothly
* Automatic, programmable text alignment and wrapping
* Simple markup for setting text attributes within blocks of text
* Powerful list box with programmable content for scrolling all
  widget types
* Your choice of event loops: Twisted, Glib or built-in
  select-based loop
* Pre-built widgets include edit boxes, buttons, check
  boxes and radio buttons
* Display modules include raw, curses, and
  experimental LCD and web displays
* Support for UTF-8, simple 8-bit and CJK encodings
* 256 and 88 color mode support

%build -p
# No git tag in the sdist. The old sed matched every "name =" line and
# stored the version on the author table.
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%files 
%{py_sitedir}/*
