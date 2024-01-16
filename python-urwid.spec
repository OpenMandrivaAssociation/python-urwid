%define debug_package %{nil}

%define module	urwid

Summary:	Full-featured Python console user interface library

Name: 		python-%{module}
Version:	2.4.2
Release:	1
Source0:	https://pypi.org/packages/source/u/urwid/%{module}-%{version}.tar.gz
License:	LGPL
Group: 		Development/Python
Url: 		http://urwid.org
BuildRequires:	python3dist(setuptools)
BuildRequires:	pkgconfig(python)

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
* Python 3.2 support

%prep
%setup -q -n %{module}-%{version}

%build
%setup_compile_flags
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE=  %__python setup.py install --root=%{buildroot}

%files 
%{py_platsitedir}/*
