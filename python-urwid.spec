%define module	urwid
%define name	python-%{module}
%define version	1.1.1
%define release 1

Summary:	Full-featured Python console user interface library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://excess.org/%{module}/%{module}-%{version}.tar.gz
License:	LGPL
Group: 		Development/Python
Url: 		http://excess.org/%{module}
BuildRequires:	python-setuptools
BuildRequires:	python-devel

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
PYTHONDONTWRITEBYTECODE=  %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files 
#-f FILE_LIST
%doc CHANGELOG  *py
%py_platsitedir/*
