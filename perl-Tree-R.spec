%include	/usr/lib/rpm/macros.perl
%define		pdir	Tree
%define		pnam	R
Summary:	Tree::R - Perl extension for the Rtree data structure and algorithms
Summary(pl):	Tree::R - rozszerzenie perla o struktury i algorytmy Rtree
Name:		perl-Tree-R
Version:	0.05
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e53d8849d7269dfe606e9bdcbb48bf72
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
R-tree is a data structure for storing and indexing and efficiently
looking up non-zero-size spatial objects.

%description -l pl
Drzewa RTree to struktury danych, s³u¿±ce do przechowywania, indeksowana
oraz wydajnego wyszukiwania elementów przestrzennych niezerowej wielko¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tree/R.pm
%{_mandir}/man3/*
