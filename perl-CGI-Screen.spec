#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Screen
Summary:	CGI::Screen - Perl extension for easy creation of multi screen CGI scripts
Summary(pl):	CGI::Screen - rozszerzenia Perla do ³atwego tworzenia wieloekranowych skryptów CGI
Name:		perl-CGI-Screen
Version:	0.122
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3bcbb56df1852bd20183cd9eda3ea6e9
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Screen is a subclass of "CGI" which allows the esay(TM) creation
of simple multi screen CGI scripts.  By 'multi screen' I mean scripts
which present different screens to the user when called with different
parameters. This is the common case for scripts linking to themselves.

%description -l pl
CGI::Screen jest podklas± "CGI", która umo¿liwia ³atwe(TM) tworzenie
wieloekranowych skryptów CGI. ,,Skrypt wieloekranowy'' oznacza tu
skrypt, który przedstawia u¿ytkownikowi ró¿ne ekrany, gdy wywo³ywany
jest z ró¿nymi parametrami. Jest to przypadek ogólny dla skryptów,
które wywo³uj± same siebie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/CGI/Screen.pm
%{_mandir}/man3/*
