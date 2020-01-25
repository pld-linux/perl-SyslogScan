#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	SyslogScan
Summary:	SyslogScan contains routines to parse system logs
Summary(pl.UTF-8):	SyslogScan zawiera funkcje do analizy logów systemowych
Name:		perl-SyslogScan
Version:	0.32
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SyslogScan/SyslogScan-%{version}.tar.gz
# Source0-md5:	d3923593207e0dbf5b26064d01518d4c
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/SyslogScan-/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SyslogScan contains routines to parse system logs.

%description -l pl.UTF-8
SyslogScan zawiera funkcje do analizy logów systemowych.

%prep
%setup -q -n SyslogScan-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%{perl_vendorlib}/SyslogScan
%{perl_vendorlib}/read_mail_log.pl
%{_mandir}/man3/*
