%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Screen perl module
Summary(pl):	Modu³ perla CGI-Screen
Name:		perl-CGI-Screen
Version:	0.122
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Screen-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
CGI-Screen - Perl extension for easy creation of multi screen CGI scripts.

%description -l pl
CGI-Screen - rozszerzenie perla u³atwiaj±ce tworzenie 'wieloekranowych' 
skryptów CGI.

%prep
%setup -q -n CGI-Screen-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI/Screen
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/CGI/Screen.pm
%{perl_sitearch}/auto/CGI/Screen

%{_mandir}/man3/*
