%include	/usr/lib/rpm/macros.perl
Summary:	SyslogScan perl module
Summary(pl):	Modu³ perla SyslogScan
Name:		perl-SyslogScan
Version:	0.32
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/SyslogScan/SyslogScan-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%{perl_sitelib}/SyslogScan
%{perl_sitelib}/read_mail_log.pl
%{_mandir}/man3/*
