#
%define		module	mutagen
#
Summary:	Audio metadata reader/writer
Name:		python-%{module}
Version:	1.1
Release:	1
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
