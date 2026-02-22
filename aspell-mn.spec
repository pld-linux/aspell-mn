Summary:	Mongolian dictionary for aspell
Summary(pl.UTF-8):	Słownik mongolski dla aspella
Name:		aspell-mn
Version:	0.06
%define	subv	2
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/mn/aspell6-mn-%{version}-%{subv}.tar.bz2
# Source0-md5:	fd1ed8b4e57c858c62c4f74a687bba90
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mongolian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik mongolski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-mn-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/Changes
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
