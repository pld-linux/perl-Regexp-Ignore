%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Ignore
Summary:	Regexp::Ignore perl module - ignore unwanted parts of text
Summary(pl):	Modu³ perla Regexp::Ignore - ignoruj±cy niechciane czêsci tekstu
Name:		perl-Regexp-Ignore
Version:	0.01
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Ignore - Let us ignore unwanted parts (e.g. tags in markup
languages as HTML), while parsing text.

%description -l pl
Modu³ Regexp::Ignore - pozwalaj±cy ignorowaæ niechciane fragmenty
(np. znaczniki w jêzykach typu HTML) podczas analizy tekstu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Regexp/Ignore*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
