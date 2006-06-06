#
%define		module	mutagen
#
Summary:	Audio metadata reader/writer
Summary(pl):	Modu³ do odczytu i zapisu metadanych d¼wiêkowych
Name:		python-%{module}
Version:	1.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.sacredchao.net/~piman/software/%{module}-%{version}.tar.gz
# Source0-md5:	4a5f656d803ea371e06eaff3fbc1dfbb
URL:		http://www.sacredchao.net/quodlibet/wiki/Development/Mutagen
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutagen is an audio metadata tag reader and writer implemented in pure
Python. It supports reading ID3v1.1, ID3v2.2, ID3v2.3, ID3v2.4, APEv2,
and FLAC, and writing ID3v1.1, ID3v2.4, APEv2, and FLAC.

%description -l pl
Mutagen to modu³ do odczytu i zapisu znaczników metadanych d¼wiêkowych
zaimplementowany w czystym Pythonie. Obs³uguje odczyt ID3v1.1,
ID3v2.2, ID3v2.3, ID3v2.4, APEv2 i FLAC oraz zapis ID3v1.1, ID3v2.4,
APEv2 i FLAC.

%package tools
Summary:	Simple tools for reading and writing audio metadata
Summary(pl):	Proste narzêdzia do odczytu i zapisu metadanych d¼wiêkowych
Group:		Application/Multimedia
Requires:	%{name} = %{version}-%{release}

%description tools
Simple tools for reading and writting audio metadata.

%description tools -l pl
Proste narzêdzia do odczytu i zapisu metadanych d¼wiêkowych.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module} -name '*.py' -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%{py_sitescriptdir}/%{module}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
