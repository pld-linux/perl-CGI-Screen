%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Screen
Summary:	CGI::Screen perl module
Summary(pl):	Modu³ perla CGI::Screen
Name:		perl-CGI-Screen
Version:	0.122
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Screen - Perl extension for easy creation of multi screen CGI
scripts.

%description -l pl
CGI::Screen - rozszerzenie perla u³atwiaj±ce tworzenie
'wieloekranowych' skryptów CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/CGI/Screen.pm
%{_mandir}/man3/*
