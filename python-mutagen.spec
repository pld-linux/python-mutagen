#
%define		module	mutagen
#
Summary:	Audio metadata reader/writer
Summary(pl.UTF-8):	Moduł do odczytu i zapisu metadanych dźwiękowych
Name:		python-%{module}
Version:	1.24
Release:	2
License:	GPL v2
Group:		Development/Languages/Python
Source0:	https://bitbucket.org/lazka/mutagen/downloads/mutagen-%{version}.tar.gz
# Source0-md5:	5cccad24a9d23aacf95baab633790217
URL:		https://bitbucket.org/lazka/mutagen/
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutagen is an audio metadata tag reader and writer implemented in pure
Python. It supports reading ID3v1.1, ID3v2.2, ID3v2.3, ID3v2.4, APEv2,
and FLAC, and writing ID3v1.1, ID3v2.4, APEv2, and FLAC.

%description -l pl.UTF-8
Mutagen to moduł do odczytu i zapisu znaczników metadanych dźwiękowych
zaimplementowany w czystym Pythonie. Obsługuje odczyt ID3v1.1,
ID3v2.2, ID3v2.3, ID3v2.4, APEv2 i FLAC oraz zapis ID3v1.1, ID3v2.4,
APEv2 i FLAC.

%package tools
Summary:	Simple tools for reading and writing audio metadata
Summary(pl.UTF-8):	Proste narzędzia do odczytu i zapisu metadanych dźwiękowych
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description tools
Simple tools for reading and writting audio metadata.

%description tools -l pl.UTF-8
Proste narzędzia do odczytu i zapisu metadanych dźwiękowych.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*.egg-info

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
