Summary:	Mongolian dictionary for aspell
Summary(pl.UTF-8):   Słownik mongolski dla aspella
Name:		aspell-mn
Version:	0.01
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/mn/aspell6-mn-%{version}-%{subv}.tar.bz2
# Source0-md5:	20aa91b99ce5e7a2b4168711398f5dfe
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
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
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
