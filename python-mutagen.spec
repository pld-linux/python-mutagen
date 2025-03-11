#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
#
%define		module	mutagen
Summary:	Audio metadata reader/writer for Python 2
Summary(pl.UTF-8):	Moduł Pythona 2 do odczytu i zapisu metadanych dźwiękowych
Name:		python-%{module}
# keep 1.43.x here for python2 support
Version:	1.43.1
Release:	3
License:	GPL v2+
Group:		Development/Languages/Python
#Source0Download: https://github.com/quodlibet/mutagen/releases
Source0:	https://github.com/quodlibet/mutagen/releases/download/release-%{version}/mutagen-%{version}.tar.gz
# Source0-md5:	90e55bbd35517c2c93859f2d922969bd
URL:		https://github.com/quodlibet/mutagen
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
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

%package tools
Summary:	Simple tools for reading and writing audio metadata
Summary(pl.UTF-8):	Proste narzędzia do odczytu i zapisu metadanych dźwiękowych
Group:		Applications/Multimedia
%if %{with python3}
Requires:	python3-%{module} = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description tools
Simple tools for reading and writting audio metadata.

%description tools -l pl.UTF-8
Proste narzędzia do odczytu i zapisu metadanych dźwiękowych.

%package -n python3-%{module}
Summary:	Audio metadata reader/writer for Python 3
Summary(pl.UTF-8):	Moduł Pythona 3 do odczytu i zapisu metadanych dźwiękowych
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Mutagen is an audio metadata tag reader and writer implemented in pure
Python. It supports reading ID3v1.1, ID3v2.2, ID3v2.3, ID3v2.4, APEv2,
and FLAC, and writing ID3v1.1, ID3v2.4, APEv2, and FLAC.

%description -n python3-%{module} -l pl.UTF-8
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
%if %{with python2}
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*
%endif
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%{py_sitescriptdir}/mutagen
%{py_sitescriptdir}/mutagen-%{version}-py*.egg-info
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mid3cp
%attr(755,root,root) %{_bindir}/mid3iconv
%attr(755,root,root) %{_bindir}/mid3v2
%attr(755,root,root) %{_bindir}/moggsplit
%attr(755,root,root) %{_bindir}/mutagen-inspect
%attr(755,root,root) %{_bindir}/mutagen-pony
%{_mandir}/man1/mid3cp.1*
%{_mandir}/man1/mid3iconv.1*
%{_mandir}/man1/mid3v2.1*
%{_mandir}/man1/moggsplit.1*
%{_mandir}/man1/mutagen-inspect.1*
%{_mandir}/man1/mutagen-pony.1*

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/mutagen
%{py3_sitescriptdir}/mutagen-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,api,man,user,*.html,*.js}
%endif
