%define		module	mutagen
#
Summary:	Audio metadata reader/writer
Name:		python-%{module}
Version:	1.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.sacredchao.net/~piman/software/%{module}-%{version}.tar.gz
# Source0-md5:	3c6d77bed3009e039459945613b05474
URL:		http://www.sacredchao.net/quodlibet/wiki/Development/Mutagen
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutagen is an audio metadata tag reader and writer implemented in pure Python.
It supports reading ID3v1.1, ID3v2.2, ID3v2.3, ID3v2.4, APEv2, and FLAC, and
writing ID3v1.1, ID3v2.4, APEv2, and FLAC.

%prep
%setup -q -n %{module}-%{version}

%build
%{__make} extensions
%{__make} po-data

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LIBDIR=%{_libdir} \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.py
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/browsers
%{_libdir}/%{name}/formats
#%{_libdir}/%{name}/mutagen
%{_libdir}/%{name}/parse
%{_libdir}/%{name}/plugins
%{_libdir}/%{name}/qltk
%{_libdir}/%{name}/util
%{_libdir}/%{name}/*.png
%{_libdir}/%{name}/*.svg
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
