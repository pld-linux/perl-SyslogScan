%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	SyslogScan perl module
Summary(pl):	Modu³ perla SyslogScan
Name:		perl-SyslogScan
Version:	0.32
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Syslog/SyslogScan-%{version}.tar.gz
Patch:		perl-SyslogScan-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
SyslogScan contains routines to parse system logs.

%description -l pl
SyslogScan zawiera rutyny do analizy logów systemowych.

%prep
%setup -q -n SyslogScan-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/SyslogScan
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,HISTORY}.gz

%{perl_sitelib}/SyslogScan
%{perl_sitelib}/read_mail_log.pl
%{perl_sitearch}/auto/SyslogScan

%{_mandir}/man3/*
