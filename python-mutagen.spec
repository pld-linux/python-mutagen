#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# unit tests
#
%define		module	mutagen
Summary:	Audio metadata reader/writer for Python 2
Summary(pl.UTF-8):	Moduł Pythona 2 do odczytu i zapisu metadanych dźwiękowych
Name:		python-%{module}
# keep 1.43.x here for python2 support
Version:	1.43.1
Release:	4
License:	GPL v2+
Group:		Development/Languages/Python
#Source0Download: https://github.com/quodlibet/mutagen/releases
Source0:	https://github.com/quodlibet/mutagen/releases/download/release-%{version}/mutagen-%{version}.tar.gz
# Source0-md5:	90e55bbd35517c2c93859f2d922969bd
URL:		https://github.com/quodlibet/mutagen
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2 >= 1.3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
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

%package apidocs
Summary:	API documentation for Python mutagen module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona mutagen
Group:		Documentation

%description apidocs
API documentation for Python mutagen module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona mutagen.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

# tools provided by python3-mutagen.spec
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%{py_sitescriptdir}/mutagen
%{py_sitescriptdir}/mutagen-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,api,man,user,*.html,*.js}
%endif
