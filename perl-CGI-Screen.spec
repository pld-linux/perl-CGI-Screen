%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Screen perl module
Summary(pl):	Modu³ perla CGI-Screen
Name:		perl-CGI-Screen
Version:	0.122
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Screen-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Screen - Perl extension for easy creation of multi screen CGI
scripts.

%description -l pl
CGI-Screen - rozszerzenie perla u³atwiaj±ce tworzenie
'wieloekranowych' skryptów CGI.

%prep
%setup -q -n CGI-Screen-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/Screen.pm
%{_mandir}/man3/*
