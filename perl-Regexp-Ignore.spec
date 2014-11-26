#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Regexp
%define		pnam	Ignore
%include	/usr/lib/rpm/macros.perl
Summary:	Regexp::Ignore Perl module - ignore unwanted parts of text
Summary(pl.UTF-8):	Moduł Perla Regexp::Ignore - ignorowanie niechcianych części tekstu
Name:		perl-Regexp-Ignore
Version:	0.03
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	542ad987adbd6da9d82494f065b45b9d
URL:		http://search.cpan.org/dist/Regexp-Ignore/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Ignore - Let us ignore unwanted parts (e.g. tags in markup
languages as HTML), while parsing text.

%description -l pl.UTF-8
Moduł Regexp::Ignore - pozwalający ignorować niechciane fragmenty (np.
znaczniki w językach typu HTML) podczas analizy tekstu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%{__perl} -pi -e 's:/usr/local/bin/perl:/usr/bin/perl:' examples/speller.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Regexp/Ignore*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
