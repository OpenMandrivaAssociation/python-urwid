%define module_name urwid
%define rel 1

Summary:    Python library to write console user interface library 
Name: 		python-%{module_name}
Version: 	0.9.8
Release: 	%mkrel %rel
Source0: 	http://excess.org/%{module_name}/%{module_name}-%{version}.tar.bz2
License:	LGPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		http://excess.org/%{module_name}
BuildRequires: python-devel

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
%setup -q -n %{module_name}-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc  *html *py 
%dir %py_platsitedir/%module_name


