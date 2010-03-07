%define upstream_name    Pod-Loom
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Do-nothing template for Pod::Loom
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(Moose)
BuildRequires: perl(PPI)
BuildRequires: perl(Pod::Eventual)
BuildRequires: perl(String::RewritePrefix)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


