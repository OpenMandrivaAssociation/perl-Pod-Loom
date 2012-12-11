%define upstream_name    Pod-Loom
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Do-nothing template for Pod::Loom
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Moose)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Pod::Eventual)
BuildRequires:	perl(String::RewritePrefix)
BuildArch:	noarch

%description
Pod::Loom extracts all the POD sections from Perl code, passes the POD to a
template that may reformat it in various ways, and then returns a copy of
the code with the reformatted POD at the end.

A template may convert non-standard POD commands like '=method' and '=attr'
into standard POD, reorder sections, and generally do whatever it likes to
the POD.

The document being reformatted can specify the template to use with a line
like this:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 656959
- rebuild for updated spec-helper

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.04

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 515367
- update to 0.03

* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 488149
- import perl-Pod-Loom


* Sat Jan 09 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
