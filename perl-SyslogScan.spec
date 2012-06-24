%include	/usr/lib/rpm/macros.perl
Summary:	SyslogScan perl module
Summary(pl):	Modu� perla SyslogScan
Name:		perl-SyslogScan
Version:	0.32
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Syslog/SyslogScan-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SyslogScan contains routines to parse system logs.

%description -l pl
SyslogScan zawiera rutyny do analizy log�w systemowych.

%prep
%setup -q -n SyslogScan-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/SyslogScan
%{perl_sitelib}/read_mail_log.pl
%{_mandir}/man3/*
