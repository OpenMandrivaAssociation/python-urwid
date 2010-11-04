%define module	urwid
%define name	python-%{module}
%define version	0.9.9.1
%define release %mkrel 3

Summary:	Python library to write console user interface library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://excess.org/%{module}/%{module}-%{version}.tar.gz
License:	LGPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Url: 		http://excess.org/%{module_name}
BuildRequires:	python-devel

%description
Urwid is a console user interface library. It includes many features
useful for text console application developers including :

* Fluid interface resizing (xterm window resizing / fbset on Linux console)
* Web application display mode using Apache and CGI [Live Demo]
* Support for UTF-8, simple 8-bit and CJK encodings
* Multiple text alignment and wrapping modes built-in
* Ability create user-defined text layout classes
* Simple markup for setting text attributes
* Powerful list box that handles scrolling between different widget types
* List box contents may be managed with a user-defined class
* Flexible edit box for editing many different types of text
* Buttons, check boxes and radio boxes
* Customizable layout for all widgets
* Easy interface for creating HTML screen shots

%prep
%setup -q -n %{module}-%{version}

%build
%setup_compile_flags
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc  *html *py
%py_platsitedir/*
