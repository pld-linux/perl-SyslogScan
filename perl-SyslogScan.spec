%include	/usr/lib/rpm/macros.perl
Summary:	SyslogScan perl module
Summary(pl):	Modu³ perla SyslogScan
Name:		perl-SyslogScan
Version:	0.32
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SyslogScan/SyslogScan-%{version}.tar.gz
# Source0-md5:	d3923593207e0dbf5b26064d01518d4c
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SyslogScan contains routines to parse system logs.

%description -l pl
SyslogScan zawiera rutyny do analizy logów systemowych.

%prep
%setup -q -n SyslogScan-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%{perl_vendorlib}/SyslogScan
%{perl_vendorlib}/read_mail_log.pl
%{_mandir}/man3/*
